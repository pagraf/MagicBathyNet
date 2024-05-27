![magicbathynet](https://github.com/pagraf/MagicBathyNet/assets/35768562/85d2f09c-2bc9-4edb-9b3e-5428589fdf64)


# MagicBathyNet: A Multimodal Remote Sensing Dataset for Benchmarking Learning-based Bathymetry and Pixel-based Classification in Shallow Waters

[MagicBathyNet](https://www.magicbathy.eu/magicbathynet.html) is a benchmark dataset made up of image patches of Sentinel-2, SPOT-6 and aerial imagery, bathymetry in raster format and seabed classes annotations. Dataset also facilitates unsupervised learning for model pre-training in shallow coastal areas.
<br />
<br />

# Package for benchmarking MagicBathyNet dataset in learning-based bathymetry and pixel-based classification.

This repository contains the code of the paper [MagicBathyNet: A Multimodal Remote Sensing Dataset for Bathymetry Prediction and Pixel-based Classification in Shallow Waters accepted for publication in the 2024 IEEE International Geoscience and Remote Sensing Symposium (IGARSS 2024)]([https://arxiv.org/abs/2405.15477]). 


## Citation

If you find this repository useful, please consider giving a star ⭐.<br />
If you use the code in this repository or the dataset please cite:

>Agrafiotis, P., Zanowski, L., Skarlatos, D. & Demir, B. (2024) MagicBathyNet: A Multimodal Remote Sensing Dataset for Bathymetry Prediction and Pixel-based Classification in Shallow Waters, arXiv preprint
arXiv:2405.15477, 2024.

```
@article{agrafiotis2024magicbathynet,
      title={MagicBathyNet: A Multimodal Remote Sensing Dataset for Bathymetry Prediction and Pixel-based Classification in Shallow Waters}, 
      author={Panagiotis Agrafiotis and Łukasz Janowski and Dimitrios Skarlatos and Begüm Demir},
      year={2024},
      journal={arXiv preprint arXiv:2405.15477}
}
```
<br />

# Getting started

## Downloading the dataset

For downloading the dataset and a detailed explanation of it, please visit the MagicBathy Project website at [https://www.magicbathy.eu/magicbathynet.html](https://www.magicbathy.eu/magicbathynet.html)


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
  ┃ ┣ 📜 [modality]_split_bathymetry.txt
  ┃ ┣ 📜 [modality]_split_pixel_class.txt
  ┃ ┣ 📜 norm_param_[modality]_an.txt
  ┃
  ┣ 📂 puck_lagoon/
  ┃ ┣ 📂 img/
  ┃ ┃ ┣ 📜 ...
  ┃ ┣ 📂 depth/
  ┃ ┃ ┣ 📜 ...
  ┃ ┣ 📂 gts/
  ┃ ┃ ┣ 📜 ...
  ┃ ┣ 📜 [modality]_split_bathymetry.txt
  ┃ ┣ 📜 [modality]_split_pixel_class.txt
  ┃ ┣ 📜 norm_param_[modality]_pl.txt
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
We provide code and model weights for the following deep learning models that have been pre-trained on MagicBathyNet for pixel-based classification and bathymetry tasks:

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
| Modified U-Net for bathymetry | Aerial | Agia Napa | [bathymetry_aerial_an.zip](https://drive.google.com/file/d/1-qUlQMHdZDZKkeQ4RLX54o4TK6juwOqD/view?usp=sharing) |
| Modified U-Net for bathymetry | Aerial | Puck Lagoon         | [bathymetry_aerial_pl.zip](https://drive.google.com/file/d/1SN8YH-WZIdR4e5Zl0uQK4OM62z_WNCks/view?usp=sharing)            |
| Modified U-Net for bathymetry | SPOT-6 | Agia Napa        | [bathymetry_spot6_an.zip](https://drive.google.com/file/d/1giG-MrJQZ2YLDzjOd2h-u2vr9gfI1jO0/view?usp=sharing)            |
| Modified U-Net for bathymetry | SPOT-6 | Puck Lagoon      | [bathymetry_spot6_pl.zip](https://drive.google.com/file/d/1Cf1gAsEUfACkBep4i_0gB-pp_L0bvaU_/view?usp=sharing)      |
| Modified U-Net for bathymetry | Sentinel-2 | Agia Napa    | [bathymetry_s2_an.zip](https://drive.google.com/file/d/15esoghCHHHilQJxTBBjmHpAAde-AHdtE/view?usp=sharing)   | 
| Modified U-Net for bathymetry | Sentinel-2 | Puck Lagoon    | [bathymetry_s2_pl.zip](https://drive.google.com/file/d/1oCnD5ePwVW3ORix4GWRcMUp_kSL5p9Se/view?usp=sharing)   |

To achieve the results presented in the paper, use the parameters and the specific train-evaluation splits provided in the dataset. Parameters can be found [here](https://drive.google.com/file/d/1gkIG99WFI6LNP7gsRvae9FZWU3blDPgv/view?usp=sharing) while train-evaluation splits are included in the dataset.

## Example testing results
Example patch of the Agia Napa area (left), pixel classification results obtained by U-Net (middle) and predicted bathymetry obtained by MagicBathy-U-Net (right). For more information on the results and accuracy achieved read our [paper](https://www.magicbathy.eu/). 


![img_410_aerial](https://github.com/pagraf/MagicBathyNet/assets/35768562/132b4166-b012-476b-9653-b511ede2c6f3)
![aerial_410_unet](https://github.com/pagraf/MagicBathyNet/assets/35768562/8a293815-87b4-4f45-b5de-c99f7c827bb5)
![depth_410_aerial](https://github.com/pagraf/MagicBathyNet/assets/35768562/7995efd7-f85e-4411-8037-4a68c9780bfb)



## Authors
Panagiotis Agrafiotis [https://www.user.tu-berlin.de/pagraf/](https://www.user.tu-berlin.de/pagraf/)

## Feedback
Feel free to give feedback, by sending an email to: agrafiotis@tu-berlin.de
<br />
<br />

# Funding
This work is part of **MagicBathy project funded by the European Union’s HORIZON Europe research and innovation programme under the Marie Skłodowska-Curie GA 101063294**. Work has been carried out at the [Remote Sensing Image Analysis group](https://rsim.berlin/). For more information about the project visit [https://www.magicbathy.eu/](https://www.magicbathy.eu/).
