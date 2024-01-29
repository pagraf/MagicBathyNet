'''
import cv2
path_to_gts = r"/home/pagraf/Desktop/magicbathy/train/gts_10.tif"
path_to_img = r"/home/pagraf/Desktop/magicbathy/train/img_10.tif"
gts = cv2.imread(path_to_gts)
gts_h, gts_w, _ = gts.shape
img = cv2.imread(path_to_img)
img_h, img_w, _ = img.shape
split_width = 256
split_height = 256


def start_points(size, split_size, overlap=0):
    points = [0]
    stride = int(split_size * (1-overlap))
    counter = 1
    while True:
        pt = stride * counter
        if pt + split_size >= size:
            points.append(size - split_size)
            break
        else:
            points.append(pt)
        counter += 1
    return points


X_points = start_points(gts_w, split_width, 0)
Y_points = start_points(gts_h, split_height, 0)

count = 0
name_gts = 'gts'
name_img = 'img'
frmt = 'tif'

for i in Y_points:
    for j in X_points:
        split_gts = gts[i:i+split_height, j:j+split_width]
        split_img = img[i:i+split_height, j:j+split_width]
        if np.mean(split_gts) > 0:
            cv2.imwrite('/home/pagraf/Desktop/magicbathy/train/split_2/{}_{}.{}'.format(name_gts, count, frmt), split_gts)
            cv2.imwrite('/home/pagraf/Desktop/magicbathy/train/split_2/{}_{}.{}'.format(name_img, count, frmt), split_img)
            count += 1

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
                data = src.read(boundless=True, window=window, fill_value=fill_value)
                data2 = src2.read(boundless=True, window=window, fill_value=fill_value)

                if np.mean(data[0]) > 0:
                    transform = kwargs['transform']
                    new_affine = rasterio.Affine(transform[0], transform[1], transform[2]+(col_off*pixsize),
                                     transform[3], transform[4], transform[5]-(row_off*pixsize))
                    with rasterio.open(f"./gts_{im_count}.tif", 'w',
                            width=width,
                            height=height,
                            count=kwargs['count'],
                            dtype=kwargs['dtype'],
                            crs=kwargs['crs'],
                            transform=new_affine) as out:
                        for band_nr, band in enumerate(data, start=1):
                            out.write(band, band_nr)
                        out.close()
                    with rasterio.open(f"./img_{im_count}.tif", 'w',
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
                    
        
        

multicrop('/home/pagraf/Desktop/magicbathy/train/gts_spot6.tif', '/home/pagraf/Desktop/magicbathy/train/img_spot6.tif', 10, 10, 6)


'''
































'''
import rasterio
from rasterio.windows import Window
from itertools import product

def multicrop(img_path, width, height, pixsize):
    #raster_data = rasterio.open(img_path)
    #raster = raster_data.read()

    im_count = 0
    fill_value = 0
    with rasterio.open(img_path) as src:
      kwargs = src.meta
      offsets = product(range(0, src.meta['width'], width), range(0, src.meta['height'], height))
      for col_off, row_off in offsets:
        window = Window(col_off=col_off, row_off=row_off, width=width, height=height)
        data = src.read(boundless=True, window=window, fill_value=fill_value)
        #print(len(data[0]))
        transform = kwargs['transform']
        new_affine = rasterio.Affine(transform[0], transform[1], transform[2]+(col_off*pixsize),
                                     transform[3], transform[4], transform[5]-(row_off*pixsize))
        with rasterio.open(f"./img_{im_count}.tif", 'w',
                            width=width,
                            height=height,
                            count=kwargs['count'],
                            dtype=kwargs['dtype'],
                            crs=kwargs['crs'],
                            transform=new_affine) as out:

            for band_nr, band in enumerate(data, start=1):
              out.write(band, band_nr)
            out.close()
        im_count += 1

        
    

multicrop('/home/pagraf/Desktop/magicbathy/img_s2_split/img_s2.tif', 200, 200, 5)

'''


































'''
import cv2

raster_list=[]

def getFiles(path):
    for file in os.listdir(path):
        if file.endswith(".tif"):
            if np.mean(cv2.imread(os.path.join(path, file)))>0:
                raster_list.append(file)
getFiles('/home/pagraf/Desktop/magicbathy/img_uav_split')
print(raster_list)
len(raster_list)
'''
