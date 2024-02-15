![image](https://github.com/pagraf/MagicBathyNet_Benchmark/assets/35768562/4d38f25a-9060-4090-b351-86dd82a438f0)


# MagicBathyNet: A Multimodal Remote Sensing Dataset for Benchmarking Learning-based Bathymetry and Pixel-based Classification in Shallow Waters

Dataset: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10470959.svg)](https://doi.org/10.5281/zenodo.10470959) <br />
Code: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10470959.svg)](https://doi.org/10.5281/zenodo.10470959) <br />
Puplication: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10470959.svg)](https://doi.org/10.5281/zenodo.10470959) <br />

MagicBathyNet is a benchmark dataset made up of image patches of Sentinel-2, SPOT-6 and aerial imagery, bathymetry in raster format and seabed classes annotations. Dataset also facilitates unsupervised learning for model pre-training in shallow coastal areas.
<br />
<br />


# Package for benchmarking MagicBathyNet dataset in learning-based bathymetry and pixel-based classification.

This repository contains the code of the paper [MagicBathyNet: A Multimodal Remote Sensing Dataset for Benchmarking Learning-based Bathymetry and Pixel-based Classification in Shallow Waters currently submitted and under review at 2024 IEEE International Geoscience and Remote Sensing Symposium (IGARSS 2024)](https://www.magicbathy.eu/). 


If you find this repository useful, please consider giving a star ⭐.
If you use the code in this repository or the dataset please cite:

>Agrafiotis, P., Zanowski, L., Skarlatos, D. & Demir, B. (2024) MagicBathyNet: A Multimodal Remote Sensing Dataset for Benchmarking Learning-based Bathymetry and Pixel-based Classification in Shallow Waters, IGARSS 2024 - 2024 IEEE International Geoscience and Remote Sensing Symposium, Athens, Greece, 2024

```
@INPROCEEDINGS{XXXXXX,
  author={XXX and Demir, Begüm},
  booktitle={IGARSS 2024 - 2024 IEEE International Geoscience and Remote Sensing Symposium}, 
  title={MagicBathyNet: A Multimodal Remote Sensing Dataset for Benchmarking Learning-based Bathymetry and Pixel-based Classification in Shallow Waters}, 
  year={2024},
  volume={},
  number={},
  pages={XXX},
  doi={XXX}}
```
<br />


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
  ┃ ┃ ┃ ┣ 📜 img_aerial_an_339.tif
  ┃ ┃ ┃ ┣ 📜 ...
  ┃ ┃ ┣ 📂 s2/
  ┃ ┃ ┃ ┣ 📜 img_s2_an_339.tif
  ┃ ┃ ┃ ┣ 📜 ...
  ┃ ┃ ┣ 📂 spot6/
  ┃ ┃ ┃ ┣ 📜 img_spot6_an_339.tif
  ┃ ┃ ┃ ┣ 📜 ...
  ┃ ┣ 📂 depth/
  ┃ ┃ ┣ 📂 aerial/
  ┃ ┃ ┃ ┣ 📜 depth_aerial_an_339.tif
  ┃ ┃ ┃ ┣ 📜 ...
  ┃ ┃ ┣ 📂 s2/
  ┃ ┃ ┃ ┣ 📜 depth_s2_an_339.tif
  ┃ ┃ ┃ ┣ 📜 ...
  ┃ ┃ ┣ 📂 spot6/
  ┃ ┃ ┃ ┣ 📜 depth_spot6_an_339.tif
  ┃ ┃ ┃ ┣ 📜 ...
  ┃ ┣ 📂 gts/
  ┃ ┃ ┣ 📂 aerial/
  ┃ ┃ ┃ ┣ 📜 gts_aerial_an_339.tif
  ┃ ┃ ┃ ┣ 📜 ...
  ┃ ┃ ┣ 📂 s2/
  ┃ ┃ ┃ ┣ 📜 gts_s2_an_339.tif
  ┃ ┃ ┃ ┣ 📜 ...
  ┃ ┃ ┣ 📂 spot6/
  ┃ ┃ ┃ ┣ 📜 gts_spot6_an_339.tif
  ┃ ┃ ┃ ┣ 📜 ...
  ┣ 📜 aerial_an.txt
  ┣ 📜 s2_an.txt
  ┣ 📜 spot6_an.txt
  ┣ 📂 puck_lagoon/
  ┃ ┣ 📂 img/
  ┃ ┃ ┣ 📂 ...
  ┃ ┣ 📂 depth/
  ┃ ┃ ┣ 📂 ...
  ┣ 📜 aerial_pl.txt
  ┣ 📜 s2_pl.txt
  ┣ 📜 spot6_pl.txt
```
The mapping between RGB color values and classes is:

```
For the Agia Napa area:
0 : (157, 157, 157), #poseidonia
1 : (255, 255, 255), #rock
2 : (159, 159, 159), #macroalgae
3 : (63, 63, 63),    #sand
4 : (0, 0, 0)}       #Undefined (black)

For the Puck Lagoon area:
0 : (157, 157, 157), #sand
1 : (255, 255, 255), #poseidonia
2 : (0, 0, 0)}       #Undefined (black)
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

## Example testing results
Example patch of the Agia Napa area (left), pixel classification results obtained by U-Net (middle) and predicted bathymetry obtained by MagicBathy-U-Net (right). For more information on the results and accuracy achieved please see our paper [MagicBathyNet: A Multimodal Remote Sensing Dataset for Benchmarking Learning-based Bathymetry and Pixel-based Classification in Shallow Waters currently submitted and under review at 2024 IEEE International Geoscience and Remote Sensing Symposium (IGARSS 2024)](https://www.magicbathy.eu/). 

![img_410_aerial](https://github.com/pagraf/MagicBathyNet/assets/35768562/132b4166-b012-476b-9653-b511ede2c6f3)
![aerial_410_unet256](https://github.com/pagraf/MagicBathyNet/assets/35768562/80c3f9ed-85d9-4b65-a505-76c5df0e6ba7)
![aerial_depth_agia_napa256](https://github.com/pagraf/MagicBathyNet/assets/35768562/be576c35-8881-440d-a8c2-c2857849cee7)

### Pretrained models
Pretrained models on MagicBathyNet dataset can be found under models/ in the downloanded dataset folder.

## Authors
Panagiotis Agrafiotis [https://www.user.tu-berlin.de/pagraf/](https://www.user.tu-berlin.de/pagraf/)

## Feedback
Feel free to give feedback, by sending an email to: agrafiotis@tu-berlin.de

# Fundinng
This work is part of **MagicBathy project funded by the European Union’s HORIZON Europe research and innovation programme under the Marie Skłodowska-Curie GA 101063294**. Work has been carried out at the [Remote Sensing Image Analysis group](https://rsim.berlin/). For more information about the project visit [https://www.magicbathy.eu/](https://www.magicbathy.eu/).
