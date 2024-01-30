'''
import rasterio
from rasterio.windows import Window
from itertools import product

def multicrop(img_path, img_path2, width, height, pixsize):
    #raster_data = rasterio.open(img_path)
    #raster = raster_data.read()

    im_count = 0
    fill_value = 0
    with rasterio.open(img_path) as src:
        with rasterio.open(img_path2) as src2:
            kwargs = src.meta
            kwargs2 = src2.meta
            offsets = product(range(0, src.meta['width'], width), range(0, src.meta['height'], height))
            for col_off, row_off in offsets:
                window = Window(col_off=col_off, row_off=row_off, width=width, height=height)
                data = src.read(boundless=False, window=window, fill_value=fill_value)
                data2 = src2.read(boundless=False, window=window, fill_value=fill_value)

                if np.mean(data[0]) != 0:
                    transform = kwargs['transform']
                    new_affine = rasterio.Affine(transform[0], transform[1], transform[2]+(col_off*pixsize),
                                     transform[3], transform[4], transform[5]-(row_off*pixsize))
                    
                    with rasterio.open(f"/home/pagraf/Desktop/magicbathy/puck_laggon/img/spot6/img_{im_count}.tif", 'w',
                                           width=width,
                                           height=height,
                                           count=kwargs2['count'],
                                           dtype=kwargs2['dtype'],
                                           crs=kwargs['crs'],
                                           transform=new_affine) as out2:
                         for band_nr2, band2 in enumerate(data2, start=1):
                            out2.write(band2, band_nr2)
                         out2.close()
                    im_count += 1
                    
        
        
multicrop('/home/pagraf/Desktop/magicbathy/puck_laggon/mask/spot6_clipped_mask.tif', '/home/pagraf/Desktop/magicbathy/puck_laggon/spot6_clipped.tif', 30, 30, 6)
'''




'''
import cv2
import os
from sklearn.model_selection import train_test_split 

raster_list=[]

def getFiles(path):
    for file in os.listdir(path):
        if file.endswith(".tif"):
            if np.mean(cv2.imread(os.path.join(path, file)))>0:    #use <0 for depths!!! IMREAD_UNCHANGED
                raster_list.append(file)
getFiles('/home/pagraf/Desktop/magicbathy/agia_napa/gts/aerial')
#raster_list.sort()
print('annotated sample:')
print(raster_list)
print('number of annotated samples:')
print(len(raster_list))


train, test = train_test_split(raster_list, test_size=0.2, random_state=1)

print('train sample:')
print(train)
print('test sample:')
print(test)
'''




