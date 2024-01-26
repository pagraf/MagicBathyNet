# MagicBathyNet_Benchmark
MagicBathyNet: A Multimodal Remote Sensing Dataset for Benchmarking Learning-based Bathymetry and Pixel-based Classification in Shallow Waters



Package for MagicBathyNet dataset benchmarking in learning-based bathymetry pixel classification.

This repository contains code of the paper "MagicBathyNet: A Multimodal Remote Sensing Dataset for Benchmarking Learning-based Bathymetry and Pixel-based Classification in Shallow Waters" currently submitted and under review at 2024 IEEE International Geoscience and Remote Sensing Symposium (IGARSS 2024). 
This work is part of MagicBathy project funded by the European Union’s HORIZON Europe research and innovation programme under the Marie Skłodowska-Curie GA 101063294. For more information about the project visit https://www.magicbathy.eu/.

If you use this code, please cite our paper given below:

as well as the dataset:



# Usage

## Downloading the dataset

For downloading the dataset and a detailed explanation, please visit the MagicBathy Project website at [https://www.magicbathy.eu/dataset.html](https://www.magicbathy.eu/dataset.html)

## Clone the repo

`git clone ...`

## Install the repo

`cd ./MagicBathyNet_Benchmark`

`pip install setup -e .`




# HySpecNet Tools
This repository contains tools for processing the HySpecNet-11k benchmark dataset. For downloading the dataset and a detailed explanation, please visit the HySpecNet website at [https://hyspecnet.rsim.berlin/](https://hyspecnet.rsim.berlin/). This work has been done at the [Remote Sensing Image Analysis group](https://rsim.berlin/) by [Martin Hermann Paul Fuchs](https://rsim.berlin/team/members/martin-hermann-paul-fuchs) and [Begüm Demir](https://rsim.berlin/team/members/begum-demir).

If you use this code, please cite our paper given below:

> M. H. P. Fuchs and B. Demir, "[HySpecNet-11k: a Large-Scale Hyperspectral Dataset for Benchmarking Learning-Based Hyperspectral Image Compression Methods,](https://arxiv.org/abs/2306.00385)" IGARSS 2023 - 2023 IEEE International Geoscience and Remote Sensing Symposium, Pasadena, CA, USA, 2023, pp. 1779-1782, doi: 10.1109/IGARSS52108.2023.10283385.
```
@INPROCEEDINGS{10283385,
  author={Fuchs, Martin Hermann Paul and Demir, Begüm},
  booktitle={IGARSS 2023 - 2023 IEEE International Geoscience and Remote Sensing Symposium}, 
  title={HySpecNet-11k: a Large-Scale Hyperspectral Dataset for Benchmarking Learning-Based Hyperspectral Image Compression Methods}, 
  year={2023},
  volume={},
  number={},
  pages={1779-1782},
  doi={10.1109/IGARSS52108.2023.10283385}}
```

## Setup
The code in this repository is tested with `Ubuntu 22.04 LTS` and `Python 3.10.6`.

### Dependencies
All dependencies are listed in the [`requirements.txt`](requirements.txt) and can be installed via the following command:
```
pip install -r requirements.txt
```

### Download
Follow the instructions on [https://hyspecnet.rsim.berlin](https://hyspecnet.rsim.berlin) to download HySpecNet-11k.

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
