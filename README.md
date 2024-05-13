![image](https://github.com/pagraf/MagicBathyNet_Benchmark/assets/35768562/4d38f25a-9060-4090-b351-86dd82a438f0)


# MagicBathyNet: A Multimodal Remote Sensing Dataset for Benchmarking Learning-based Bathymetry and Pixel-based Classification in Shallow Waters

[MagicBathyNet](https://www.magicbathy.eu/dataset.html) is a benchmark dataset made up of image patches of Sentinel-2, SPOT-6 and aerial imagery, bathymetry in raster format and seabed classes annotations. Dataset also facilitates unsupervised learning for model pre-training in shallow coastal areas.
<br />
<br />

# Package for benchmarking MagicBathyNet dataset in learning-based bathymetry and pixel-based classification.

This repository contains the code of the paper [MagicBathyNet: A Multimodal Remote Sensing Dataset for Benchmarking Learning-based Bathymetry and Pixel-based Classification in Shallow Waters accepted for publication in the 2024 IEEE International Geoscience and Remote Sensing Symposium (IGARSS 2024)](https://www.magicbathy.eu/). 


## Citation

If you find this repository useful, please consider giving a star ⭐.<br />
If you use the code in this repository or the dataset please cite:

>Agrafiotis, P., Zanowski, L., Skarlatos, D. & Demir, B. (2024) MagicBathyNet: A Multimodal Remote Sensing Dataset for Benchmarking Learning-based Bathymetry and Pixel-based Classification in Shallow Waters, IGARSS 2024 - 2024 IEEE International Geoscience and Remote Sensing Symposium, Athens, Greece, 2024

```
@inproceedings{agrafiotismagic,
  title={MagicBathyNet: A Multimodal Remote Sensing Dataset for Benchmarking Learning-based Bathymetry and Pixel-based Classification in Shallow Waters},
  author={Agrafiotis, P. and Zanowski, L. and Skarlatos, D. and Demir, B.},
  booktitle={IGARSS 2024-2024 IEEE International Geoscience and Remote Sensing Symposium},
  pages={},
  year={2024},
  organization={IEEE}
}
```
<br />
Agrafiotis, P., Zanowski, L., Skarlatos, D. & Demir, B. (2024) MagicBathyNet: A Multimodal Remote Sensing Dataset for Benchmarking Learning-based Bathymetry and Pixel-based Classification in Shallow Waters, IGARSS 2024 - 2024 IEEE International Geoscience and Remote Sensing Symposium, Athens, Greece, 2024

# Getting started

## Downloading the dataset

For downloading the dataset and a detailed explanation of it, please visit the MagicBathy Project website at [https://www.magicbathy.eu/dataset.html](https://www.magicbathy.eu/dataset.html)


## Dataset structure
The folder structure should be as follows:
```
┗ 📂 magicbathynet/
  ┣ 📂 agia_napa/
  ┃ ┣ 📂 img/
  ┃ ┃ ┣ 📂 aerial/
  ┃ ┃ ┃ ┣ 📜 img_339.tif
  ┃ ┃ ┃ ┣ 📜 ...
  ┃ ┃ ┣ 📂 s2/
  ┃ ┃ ┃ ┣ 📜 img_339.tif
  ┃ ┃ ┃ ┣ 📜 ...
  ┃ ┃ ┣ 📂 spot6/
  ┃ ┃ ┃ ┣ 📜 img_339.tif
  ┃ ┃ ┃ ┣ 📜 ...
  ┃ ┣ 📂 depth/
  ┃ ┃ ┣ 📂 aerial/
  ┃ ┃ ┃ ┣ 📜 depth_339.tif
  ┃ ┃ ┃ ┣ 📜 ...
  ┃ ┃ ┣ 📂 s2/
  ┃ ┃ ┃ ┣ 📜 depth_339.tif
  ┃ ┃ ┃ ┣ 📜 ...
  ┃ ┃ ┣ 📂 spot6/
  ┃ ┃ ┃ ┣ 📜 depth_339.tif
  ┃ ┃ ┃ ┣ 📜 ...
  ┃ ┣ 📂 gts/
  ┃ ┃ ┣ 📂 aerial/
  ┃ ┃ ┃ ┣ 📜 gts_339.tif
  ┃ ┃ ┃ ┣ 📜 ...
  ┃ ┃ ┣ 📂 s2/
  ┃ ┃ ┃ ┣ 📜 gts_339.tif
  ┃ ┃ ┃ ┣ 📜 ...
  ┃ ┃ ┣ 📂 spot6/
  ┃ ┃ ┃ ┣ 📜 gts_339.tif
  ┃ ┃ ┃ ┣ 📜 ...
  ┃ ┣ 📂 pretrained_models/
  ┃ ┣ 📜 aerial_split.txt
  ┃ ┣ 📜 s2_split.txt
  ┃ ┣ 📜 spot6_split.txt
  ┃
  ┣ 📂 puck_lagoon/
  ┃ ┣ 📂 img/
  ┃ ┃ ┣ 📜 ...
  ┃ ┣ 📂 depth/
  ┃ ┃ ┣ 📜 ...
  ┃ ┣ 📂 gts/
  ┃ ┃ ┣ 📜 ...
  ┃ ┣ 📂 pretrained_models/
  ┃ ┣ 📜 aerial_split.txt
  ┃ ┣ 📜 s2_split.txt
  ┃ ┣ 📜 spot6_split.txt
```
The mapping between RGB color values and classes is:

```
For the Agia Napa area:
0 : (0, 128, 0),   #seagrass
1 : (0, 0, 255),   #rock
2 : (255, 0, 0),   #macroalgae
3 : (255, 128, 0), #sand
4 : (0, 0, 0)}     #Undefined (black)

For the Puck Lagoon area:
0 : (255, 128, 0), #sand
1 : (0, 128, 0) ,  #eelgrass/pondweed
2 : (0, 0, 0)}     #Undefined (black)
```


## Setup
The code in this repository is tested with `Ubuntu 22.04 LTS` and `Python 3.8.10` `GCC 9.4.0`.

## Clone the repo

`git clone ...`

## Install the repo

`cd ./MagicBathyNet_Benchmark`

`pip install setup -e .`

### Dependencies
All dependencies are listed in the [`requirements.txt`](requirements.txt) and can be installed via the following command:
```
pip install -r requirements.txt
```

## Train and Test the models
To train and test the **bathymetry** models use **MagicBathy_Benchmarking_Bathymetry.ipynb**.

To train and test the **pixel-based classification** models use **MagicBathy_Benchmarking_semsegm.ipynb**.

## Pre-trained Deep Learning Models
We provide code and model weights for the following deep learning models that have been pre-trained on BigEarthNet-S2 with the original Level-3 class nomenclature of CLC 2018 (which includes 43 classes) for scene classification:

### Pixel-based classification
| Model Names | Modality | Area | Pre-Trained PyTorch Models                                                                                                                | 
| ----------- |----------| ---- |----------------------------------------------------------------------------------------------------------------------------------------------|
| U-Net | Aerial | Agia Napa | [unet_aerial_an.zip](https://drive.google.com/file/d/1vrYwOGEPbiuyvAmtE8-SfbDfzVWU8oMD/view?usp=sharing) |
| SegFormer | Aerial | Agia Napa         | [segformer_aerial_an.zip](https://drive.google.com/file/d/1rUr_KvAgOKwBmykLoprUy4Aw4fCiYGIm/view?usp=sharing)            |
| U-Net | Aerial | Puck Lagoon | [unet_aerial_pl.zip](https://drive.google.com/file/d/1PVIRvFpiw4xf6xgLCF4Bzhpb_2wD3Q3G/view?usp=sharing) |
| SegFormer | Aerial | Puck Lagoon         | [segformer_aerial_pl.zip](https://drive.google.com/file/d/1c_YNKXvANd71piMEmGOa1hdo6J58ZynP/view?usp=sharing)            |
| U-Net | SPOT-6 | Agia Napa        | [unet_spot6_an.zip](https://drive.google.com/file/d/1GNpk6zG-t0e853B5ntd5ETJEeyShnMkL/view?usp=sharing)            |
| SegFormer | SPOT-6 | Agia Napa      | [segformer_spot6_an.zip](https://drive.google.com/file/d/198k981Qdvw8Y5eZ8sMGVDIcPC8B-uDkx/view?usp=sharing)      |
| U-Net | SPOT-6 | Puck Lagoon        | [unet_spot6_pl.zip](https://drive.google.com/file/d/1h3jZ-QY8xiI6Q4O7jXO3BzZDyO08W1A0/view?usp=sharing)            |
| SegFormer | SPOT-6 | Puck Lagoon      | [segformer_spot6_pl.zip](https://drive.google.com/file/d/12p4AdmHgK0PWsxJ6x2pedqqzfkJ2f4E-/view?usp=sharing )      |
| U-Net | Sentinel-2 | Agia Napa     | [unet_s2_an.zip](https://drive.google.com/file/d/19FeZ60AK67z-DCFWhjqDrV6-Xlyicgqn/view?usp=sharing)   | 
| SegFormer | Sentinel-2 | Agia Napa    | [segformer_s2_an.zip](https://drive.google.com/file/d/1nOKhVecid3yjAg0fF-rTV2-cGmUMj6nh/view?usp=sharing)   |
| U-Net | Sentinel-2 | Puck Lagoon    | [unet_s2_pl.zip](https://drive.google.com/file/d/1iySJta5qPegW7TEy5yIiFvqr816THEuY/view?usp=sharing)   | 
| SegFormer | Sentinel-2 | Puck Lagoon    | [segformer_s2_pl.zip](https://drive.google.com/file/d/1T7iP7khBBK0YsQzdUHAUksX9Q_Qbw5kW/view?usp=sharing)   |

### Learning-based Bathymetry
| Model Name | Modality | Area | Pre-Trained PyTorch Models                                                                                                                | 
| ----------- |----------| ---- |----------------------------------------------------------------------------------------------------------------------------------------------|
| Image2Bathy | Aerial | Agia Napa | [Image2Bathy_aerial_an.zip](http://bigearth.net/static/pretrained-models/BigEarthNet-S2_43-Classes/K-BranchCNN.zip) |
| Image2Bathy | Aerial | Puck Lagoon         | [Image2Bathy_aerial_pl.zip](http://bigearth.net/static/pretrained-models/BigEarthNet-S2_43-Classes/VGG16.zip)            |
| Image2Bathy | SPOT-6 | Agia Napa        | [Image2Bathy_spot6_an.zip](http://bigearth.net/static/pretrained-models/BigEarthNet-S2_43-Classes/VGG19.zip)            |
| Image2Bathy | SPOT-6 | Puck Lagoon      | [Image2Bathy_spot6_pl.zip](http://bigearth.net/static/pretrained-models/BigEarthNet-S2_43-Classes/ResNet50.zip)      |
| Image2Bathy | Sentinel-2 | Agia Napa    | [Image2Bathy_s2_an.zip](http://bigearth.net/static/pretrained-models/BigEarthNet-S2_43-Classes/ResNet101.zip)   | 
| Image2Bathy | Sentinel-2 | Puck Lagoon    | [Image2Bathy_s2_pl.zip](http://bigearth.net/static/pretrained-models/BigEarthNet-S2_43-Classes/ResNet152.zip)   |


## Example testing results
Example patch of the Agia Napa area (left), pixel classification results obtained by U-Net (middle) and predicted bathymetry obtained by MagicBathy-U-Net (right). For more information on the results and accuracy achieved please see our [paper](https://www.magicbathy.eu/). 


![img_410_aerial](https://github.com/pagraf/MagicBathyNet/assets/35768562/132b4166-b012-476b-9653-b511ede2c6f3)
![aerial_410_segformer](https://github.com/pagraf/MagicBathyNet/assets/35768562/8a293815-87b4-4f45-b5de-c99f7c827bb5)
![aerial_depth_agia_napa256](https://github.com/pagraf/MagicBathyNet/assets/35768562/be576c35-8881-440d-a8c2-c2857849cee7)

## Authors
Panagiotis Agrafiotis [https://www.user.tu-berlin.de/pagraf/](https://www.user.tu-berlin.de/pagraf/)

## Feedback
Feel free to give feedback, by sending an email to: agrafiotis@tu-berlin.de
<br />
<br />

# Funding
This work is part of **MagicBathy project funded by the European Union’s HORIZON Europe research and innovation programme under the Marie Skłodowska-Curie GA 101063294**. Work has been carried out at the [Remote Sensing Image Analysis group](https://rsim.berlin/). For more information about the project visit [https://www.magicbathy.eu/](https://www.magicbathy.eu/).
