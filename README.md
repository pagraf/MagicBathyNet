![image](https://github.com/pagraf/MagicBathyNet_Benchmark/assets/35768562/4d38f25a-9060-4090-b351-86dd82a438f0)


# MagicBathyNet_Benchmark
MagicBathyNet: A Multimodal Remote Sensing Dataset for Benchmarking Learning-based Bathymetry and Pixel-based Classification in Shallow Waters

MagicBathyNet is a benchmark dataset made up of image patches of Sentinel-2, SPOT-6 and aerial imagery, bathymetry in raster format and seabed classes annotations. Dataset also facilitates unsupervised learning for model pre-training in shallow coastal areas.





## Package for benchmarking MagicBathyNet dataset in learning-based bathymetry pixel classification.

This repository contains the code of the paper "MagicBathyNet: A Multimodal Remote Sensing Dataset for Benchmarking Learning-based Bathymetry and Pixel-based Classification in Shallow Waters" currently submitted and under review at 2024 IEEE International Geoscience and Remote Sensing Symposium (IGARSS 2024). 
This work is part of MagicBathy project funded by the European Union’s HORIZON Europe research and innovation programme under the Marie Skłodowska-Curie GA 101063294. Work has been carried out at the [Remote Sensing Image Analysis group](https://rsim.berlin/). For more information about the project visit [https://www.magicbathy.eu/](https://www.magicbathy.eu/).

If you find this repository useful, please consider giving a star ⭐ and if you use the code or the dataset a citation:

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

as well as the dataset:


# Usage

## Downloading the dataset

For downloading the dataset and a detailed explanation, please visit the MagicBathy Project website at [https://www.magicbathy.eu/dataset.html](https://www.magicbathy.eu/dataset.html)

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

### Download
Follow the instructions on [https://www.magicbathy.eu/dataset.html](https://www.magicbathy.eu/dataset.html) to download MagicBathyNet.

The folder structure should be as follows:
```
┗ 📂 hyspecnet-11k/
  ┣ 📂 patches/
  ┃ ┣ 📂 tile_001/
  ┃ ┃ ┣ 📂 tile_001-patch_01/
  ┃ ┃ ┃ ┣ 📜 tile_001-patch_01-DATA.npy
  ┃ ┃ ┃ ┣ 📜 tile_001-patch_01-QL_PIXELMASK.TIF
  ┃ ┃ ┃ ┣ 📜 tile_001-patch_01-QL_QUALITY_CIRRUS.TIF
  ┃ ┃ ┃ ┣ 📜 tile_001-patch_01-QL_QUALITY_CLASSES.TIF
  ┃ ┃ ┃ ┣ 📜 tile_001-patch_01-QL_QUALITY_CLOUD.TIF
  ┃ ┃ ┃ ┣ 📜 tile_001-patch_01-QL_QUALITY_CLOUDSHADOW.TIF
  ┃ ┃ ┃ ┣ 📜 tile_001-patch_01-QL_QUALITY_HAZE.TIF
  ┃ ┃ ┃ ┣ 📜 tile_001-patch_01-QL_QUALITY_SNOW.TIF
  ┃ ┃ ┃ ┣ 📜 tile_001-patch_01-QL_QUALITY_TESTFLAGS.TIF
  ┃ ┃ ┃ ┣ 📜 tile_001-patch_01-QL_SWIR.TIF
  ┃ ┃ ┃ ┣ 📜 tile_001-patch_01-QL_VNIR.TIF
  ┃ ┃ ┃ ┣ 📜 tile_001-patch_01-SPECTRAL_IMAGE.TIF
  ┃ ┃ ┃ ┗ 📜 tile_001-patch_01-THUMBNAIL.jpg
  ┃ ┃ ┣ 📂 tile_001-patch_02/
  ┃ ┃ ┃ ┗ 📜 ...
  ┃ ┃ ┗ 📂 ...
  ┃ ┣ 📂 tile_002/
  ┃ ┃ ┗ 📂 ...
  ┃ ┗ 📂 ...
  ┗ 📂 splits/
  ┣ 📂 easy/
  ┃ ┣ 📜 test.csv
  ┃ ┣ 📜 train.csv
  ┃ ┗ 📜 val.csv
  ┣ 📂 hard/
  ┃ ┣ 📜 test.csv
  ┃ ┣ 📜 train.csv
  ┃ ┗ 📜 val.csv
  ┗ 📂 ...
```
