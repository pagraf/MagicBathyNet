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
                if np.mean(data[0]) != 0:
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






