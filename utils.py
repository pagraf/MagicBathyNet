#This script crops windows of a specified size from two raster images and create new raster files for the second 
#image based on the condition that the mean pixel value of the corresponding window in the main image is not zero


import rasterio
from rasterio.windows import Window
from itertools import product
import numpy as np

def multicrop(img_path, img_path2, width, height, pixsize):
    # Initialize image count
    im_count = 0
    
    # Fill value for rasterio read (if necessary)
    fill_value = 0
    
    # Open the main image and the second image for cropping
    with rasterio.open(img_path) as src:
        with rasterio.open(img_path2) as src2:
            # Get metadata for both images
            kwargs = src.meta
            kwargs2 = src2.meta
            
            # Generate window offsets using the specified width and height
            offsets = product(range(0, src.meta['width'], width), range(0, src.meta['height'], height))
            
            # Iterate over each window
            for col_off, row_off in offsets:
                # Create a window based on the current offset
                window = Window(col_off=col_off, row_off=row_off, width=width, height=height)
                
                # Read the data from both images for the current window
                data = src.read(boundless=False, window=window, fill_value=fill_value)
                data2 = src2.read(boundless=False, window=window, fill_value=fill_value)

                # Check if the mean pixel value of the main image is not zero
                if np.mean(data[0]) != 0:     #replace 0 with 50 for Agia Napa UAV spit
                    # Adjust the affine transformation to match the new window
                    transform = kwargs['transform']
                    new_affine = rasterio.Affine(transform[0], transform[1], transform[2] + (col_off * pixsize),
                                                 transform[3], transform[4], transform[5] - (row_off * pixsize))
                    
                    # Create a new raster file for the cropped image
                    with rasterio.open(f"/home/pagraf/Desktop/magicbathy/puck_laggon/img/spot6/img_{im_count}.tif",
                                       'w',
                                       width=width,
                                       height=height,
                                       count=kwargs2['count'],
                                       dtype=kwargs2['dtype'],
                                       crs=kwargs['crs'],
                                       transform=new_affine) as out2:
                        # Write each band of the second image to the new raster file
                        for band_nr2, band2 in enumerate(data2, start=1):
                            out2.write(band2, band_nr2)
                        
                        # Close the new raster file
                        out2.close()
                    
                    # Increment the image count
                    im_count += 1

# Example usage of the multicrop function
multicrop('/home/pagraf/Desktop/magicbathy/puck_laggon/mask/spot6_clipped_mask.tif',
          '/home/pagraf/Desktop/magicbathy/puck_laggon/spot6_clipped.tif',
          30, 30, 6)




#This script collects filenames of ".tif" files from a specified directory based on a condition related 
#to the mean pixel value of the images. It then splits the list of filenames into training and testing sets using 
#train_test_split from scikit-learn. The print statements provide information about the collected filenames and the 
#split sets.


import cv2
import os
import numpy as np
from sklearn.model_selection import train_test_split

# List to store file names
raster_list = []

# Function to get files from a specified path
def getFiles(path):
    for file in os.listdir(path):
        # Check if the file has a ".tif" extension
        if file.endswith(".tif"):
            # Read the image using OpenCV and calculate the mean pixel value
            if np.mean(cv2.imread(os.path.join(path, file))) > 0:
                # Append the file name to the list if the mean pixel value is greater than 0
                raster_list.append(file)

# Specify the path from which to get the files
getFiles('/home/pagraf/Desktop/magicbathy/agia_napa/gts/aerial')

# Print information about the annotated samples
print('annotated sample:')
print(raster_list)
print('number of annotated samples:')
print(len(raster_list))

# Split the list of file names into training and testing sets
train, test = train_test_split(raster_list, test_size=0.2, random_state=1)

# Print the training and testing sets
print('train sample:')
print(train)
print('test sample:')
print(test)




#This script privides train-test splits based on the availability of data between modalities i.e. if img and depth are both not empty.

import cv2
import os
import numpy as np
from sklearn.model_selection import train_test_split

img_path = 'path'
depth_path = 'path'

img_raster_list = []
depth_raster_list = []

def getFiles(path, raster_list):
    for file in os.listdir(path):
        if file.endswith(".tif"):
            img = cv2.imread(os.path.join(path, file), cv2.IMREAD_UNCHANGED)
            if np.mean(img) > 0:
                depth_file = file.replace("aerial", "depth")
                depth_img = cv2.imread(os.path.join(depth_path, depth_file), cv2.IMREAD_UNCHANGED)
                if np.mean(depth_img) < 0:
                    raster_list.append(file)

getFiles(img_path, img_raster_list)

paired_list = img_raster_list

train, test = train_test_split(paired_list, test_size=0.2, random_state=1)

print('train sample:')
print(train)
print('test sample:')
print(test)



#create normalization files

import os
import numpy as np
import rasterio
import matplotlib.pyplot as plt

k=4

# Directory containing the image files
image_dir = os.path.join(MAIN_FOLDER, 'agia_napa/img/spot6')

# Initialize lists to store pixel values for each channel
channel_pixel_values = [[] for _ in range(3)]  # Assuming 3 channels; adjust if needed

# Iterate through each image file in the directory
for filename in os.listdir(image_dir):
    if filename.endswith('.tif'):
        # Open the image file using rasterio
        with rasterio.open(os.path.join(image_dir, filename)) as src:
            # Read the pixel values as a 3D numpy array (bands, rows, columns)
            image_data = src.read()

            # Iterate through each channel
            for i in range(3):
                # Flatten the pixel values for the current channel to a 1D array
                channel_pixel_values[i].extend(image_data[i].flatten())

# Convert the lists of pixel values for each channel to numpy arrays
channel_pixel_values = [np.array(values) for values in channel_pixel_values]

# Calculate mean, standard deviation, and maximum for each channel across all images
channel_means = [round(np.mean(values), 3) for values in channel_pixel_values]
channel_mins = [0 for values in channel_pixel_values]
channel_stds = [round(np.std(values), 3) for values in channel_pixel_values]
channel_maxs = [round(mean + k * std, 3) for mean, std in zip(channel_means, channel_stds)]  # Calculating max based on mean and std
# Combine min and max values for each channel into a 2x3 array
norm_params = np.array([channel_mins, channel_maxs])

# Save the normalization parameters to a file
np.save('norm_param_s2_an.npy', norm_params)

print(norm_params)



#replace colors in gts
import os
from osgeo import gdal
from PIL import Image
import numpy as np

def replace_colors(image, color_mapping):
    
    #Replace specific colors in the image according to the provided mapping.

    #Parameters:
        #image (PIL.Image): The input image.
        #color_mapping (dict): A dictionary where keys are old colors (RGB tuples)
                              #and values are corresponding new colors (RGB tuples).

    #Returns:
    #    PIL.Image: The modified image.
    
    data = image.getdata()
    new_data = []
    for item in data:
        new_color = color_mapping.get(item)
        if new_color:
            new_data.append(new_color)
        else:
            new_data.append(item)
    image.putdata(new_data)
    return image

def process_geotiff(input_path, output_path, color_mapping):
    
    #Process a GeoTIFF image, replace specific colors according to the provided mapping,
    #and write back with georeference.

    #Parameters:
    #    input_path (str): Path to the input GeoTIFF image.
    #    output_path (str): Path to save the modified GeoTIFF image.
    #    color_mapping (dict): A dictionary where keys are old colors (RGB tuples)
                              #and values are corresponding new colors (RGB tuples).
    
    # Open the GeoTIFF image
    dataset = gdal.Open(input_path, gdal.GA_ReadOnly)

    # Read geotransform
    geotransform = dataset.GetGeoTransform()

    # Read raster data
    raster = dataset.ReadAsArray()

    # Close the dataset
    dataset = None

    # Convert raster array to PIL Image
    image = Image.fromarray(raster.transpose(1, 2, 0))

    # Replace colors
    modified_image = replace_colors(image, color_mapping)

    # Convert modified image back to numpy array
    modified_raster = np.array(modified_image)

    # Write modified raster back to GeoTIFF
    driver = gdal.GetDriverByName('GTiff')
    out_dataset = driver.Create(output_path, modified_raster.shape[1], modified_raster.shape[0], 3, gdal.GDT_Byte)

    # Set geotransform
    out_dataset.SetGeoTransform(geotransform)

    # Write modified raster data
    out_dataset.GetRasterBand(1).WriteArray(modified_raster[:,:,0])
    out_dataset.GetRasterBand(2).WriteArray(modified_raster[:,:,1])
    out_dataset.GetRasterBand(3).WriteArray(modified_raster[:,:,2])

    # Close output dataset
    out_dataset = None

    print("Image processed and saved successfully.")

# Specify input and output directories
input_dir = "/home/pagraf/Desktop/magicbathy/puck_laggon/gts/s2"
output_dir = "/home/pagraf/Desktop/magicbathy/puck_laggon/gts/s2_recoloured"

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define color mapping
color_mapping = {
    (157, 157, 157): (255, 128, 0), 
    (255, 255, 255): (0, 128, 0)
}

# Process each TIFF file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".tif"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        process_geotiff(input_path, output_path, color_mapping)


