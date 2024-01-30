![image](https://github.com/pagraf/MagicBathyNet_Benchmark/assets/35768562/4d38f25a-9060-4090-b351-86dd82a438f0)


# MagicBathyNet_Benchmark
MagicBathyNet: A Multimodal Remote Sensing Dataset for Benchmarking Learning-based Bathymetry and Pixel-based Classification in Shallow Waters

MagicBathyNet is a benchmark dataset made up of image patches of Sentinel-2, SPOT-6 and aerial imagery, bathymetry in raster format and seabed classes annotations. Dataset also facilitates unsupervised learning for model pre-training in shallow coastal areas.





## Package for benchmarking MagicBathyNet dataset in learning-based bathymetry pixel classification.

This repository contains the code of the paper "MagicBathyNet: A Multimodal Remote Sensing Dataset for Benchmarking Learning-based Bathymetry and Pixel-based Classification in Shallow Waters" currently submitted and under review at 2024 IEEE International Geoscience and Remote Sensing Symposium (IGARSS 2024). 
This work is part of MagicBathy project funded by the European Union’s HORIZON Europe research and innovation programme under the Marie Skłodowska-Curie GA 101063294. Work has been carried out at the [Remote Sensing Image Analysis group](https://rsim.berlin/). For more information about the project visit [https://www.magicbathy.eu/](https://www.magicbathy.eu/).

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

# Usage

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
  ┣ 📜 aerial.txt
  ┣ 📜 s2.txt
  ┣ 📜 spot6.txt
  ┣ 📂 puck_lagoon/
  ┃ ┣ 📂 img/
  ┃ ┃ ┣ 📂 ...
  ┃ ┣ 📂 depth/
  ┃ ┃ ┣ 📂 ...
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
  ┣ 📜 aerial.txt
  ┣ 📜 s2.txt
  ┣ 📜 spot6.txt
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
### Pretrained models
To download the pretrained models on MagicBAthyNet dataset press here. Then, you should create and put these items in the semanticsegmentation/trained_models/ folder.


