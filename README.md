<div align="center">
  <img src="images/icedata-logo-slogan.png" alt="logo" width="400px" style="display: block; margin-left: auto; margin-right: auto"/>
  <h2><b>Datasets Hub for the IceVision Framework</b></h2>
</div>

* * * * *
>**Note: We Need Your Help**
    If you find this work useful, please let other people know by **starring** it,
    and sharing it. 
    Thank you!
    
<div align="center">
  
[![tests](https://github.com/airctic/icedata/workflows/tests/badge.svg?event=push)](https://github.com/airctic/icedata/actions?query=workflow%3Atests)
[![docs](https://github.com/airctic/icedata/workflows/docs/badge.svg)](https://airctic.github.io/icedata/)
[![codecov](https://codecov.io/gh/airctic/icedata/branch/master/graph/badge.svg)](https://codecov.io/gh/airctic/icedata)
[![PyPI version](https://badge.fury.io/py/icedata.svg)](https://badge.fury.io/py/icedata)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/airctic/icevision/blob/master/LICENSE)  

[![Discord](https://img.shields.io/discord/735877944085446747?label=Discord&logo=Discord)](https://discord.gg/2jqrwrQ)

</div>


* * * * *


<!-- Not included in docs - start -->
## **Contributors**

[![](https://sourcerer.io/fame/lgvaz/airctic/icedata/images/0)](https://sourcerer.io/fame/lgvaz/airctic/icedata/links/0)[![](https://sourcerer.io/fame/lgvaz/airctic/icedata/images/1)](https://sourcerer.io/fame/lgvaz/airctic/icedata/links/1)[![](https://sourcerer.io/fame/lgvaz/airctic/icedata/images/2)](https://sourcerer.io/fame/lgvaz/airctic/icedata/links/2)[![](https://sourcerer.io/fame/lgvaz/airctic/icedata/images/3)](https://sourcerer.io/fame/lgvaz/airctic/icedata/links/3)[![](https://sourcerer.io/fame/lgvaz/airctic/icedata/images/4)](https://sourcerer.io/fame/lgvaz/airctic/icedata/links/4)[![](https://sourcerer.io/fame/lgvaz/airctic/icedata/images/5)](https://sourcerer.io/fame/lgvaz/airctic/icedata/links/5)[![](https://sourcerer.io/fame/lgvaz/airctic/icedata/images/6)](https://sourcerer.io/fame/lgvaz/airctic/icedata/links/6)[![](https://sourcerer.io/fame/lgvaz/airctic/icedata/images/7)](https://sourcerer.io/fame/lgvaz/airctic/icedata/links/7)

![](images/docs.png) [ **Documentation**](https://airctic.github.io/icedata/)

## Installation

```bash
pip install icedata
```

For more installation options, check our extensive [documentation](https://airctic.github.io/icevdata/install/).

**Important:** We currently only support Linux/MacOS.
<!-- Not included in docs - end -->

## Why IceData?

- IceData is a dataset hub for the [IceVision](https://github.com/airctic/icevision) Framework

- It includes community maintained datasets and parsers and has out-of-the-box support for common annotation formats (COCO, VOC, etc.)

- It provides an overview of each included dataset with a description, an annotation example, and other helpful information

- It makes end-to-end training straightforward thanks to IceVision's unified API

- It enables practioners to get moving with object detection technology quickly

## Datasets

[**Source**](https://github.com/airctic/icedata/tree/master/icedata/datasets)

The `Datasets` class is designed to simplify loading and parsing a wide range of computer vision datasets.

**Main Features:**

- Caches data so you don't need to download it over and over

- Lightweight and fast

- Transparent and pythonic API

- Out-of-the-box parsers convert common dataset annotation formats into the unified IceVision Data Format

IceData provides several ready-to-use datasets that use both common annotation formats such as COCO and VOC as well as other annotation formats such [WheatParser](https://airctic.github.io/icevision/custom_parser/) used in the [Kaggle Global Wheat Competition](https://www.kaggle.com/c/global-wheat-detection)

## Usage

Object detection datasets use multiple annotation formats (COCO, VOC, and others). IceVision makes it easy to work across all of them with its easy-to-use and extend parsers.


### COCO and VOC compatible datasets
For COCO or VOC compatible datasets - especially ones that are not include in IceData - it is easiest to use the IceData
COCO or VOC parser.

**Example:** Raccoon - a dataset using the VOC parser

```python
# Imports
from icevision.all import *
import icedata


# WARNING: Make sure you have already cloned the raccoon dataset using the command shown here above
# Set images and annotations directories
data_dir = Path("raccoon_dataset")
images_dir = data_dir / "images"
annotations_dir = data_dir / "annotations"

# Define the class_map
class_map = ClassMap(["raccoon"])

# Create a parser for dataset using the predefined icevision VOC parser
parser = parsers.voc(
    annotations_dir=annotations_dir, images_dir=images_dir, class_map=class_map
)

# Parse the annotations to create the train and validation records
train_records, valid_records = parser.parse()
show_records(train_records[:3], ncols=3, class_map=class_map)
```

!!! info "Note" 
    Notice how we use the predifined [parsers.voc()](https://github.com/airctic/icevision/blob/master/icevision/parsers/voc_parser.py) function:
    
    **parser = parsers.voc(
    annotations_dir=annotations_dir, images_dir=images_dir, class_map=class_map
    )**


### Datasets included in IceData
Datasets included in IceData always have their own parser. It can be invoked with `icedata.`datasetname`.parser(...)`.

**Example:** The IceData Fridge dataset

Please check out the [fridge folder](https://github.com/airctic/icedata/tree/master/icedata/datasets/fridge) for more information on how this dataset is structured.

```python
# Imports
from icevision.all import *
import icedata

# Load the Fridge Objects dataset
data_dir = icedata.fridge.load()

# Get the class_map
class_map = icedata.fridge.class_map()

# Parse the annotations
parser = icedata.fridge.parser(data_dir, class_map)
train_records, valid_records = parser.parse()

# Show images with their boxes and labels
show_records(train_records[:3], ncols=3, class_map=class_map)
```

!!! info "Note" 
    Notice how we use the parser associated with the fridge dataset [icedata.fridge.parser()](https://github.com/airctic/icedata/blob/master/icedata/datasets/fridge/parsers.py):
    
    **parser = icedata.fridge.parser(data_dir, class_map)**


### Datasets with a new annotation format

Sometimes, you will need to define a new annotation format for you dataset. Additional information can be found in the [documentation](https://airctic.com/custom_parser/). In this case, we strongly recommend you following the file structure and naming conventions used in the  examples such as the [Fridge dataset](https://github.com/airctic/icedata/tree/master/icedata/datasets/fridge), or the [PETS dataset](https://github.com/airctic/icedata/tree/master/icedata/datasets/pets).

![image](https://airctic.github.io/icedata/images/datasets-folder-structure.png)

# Disclaimer

Inspired from the excellent HuggingFace [Datasets](https://github.com/huggingface/datasets) project, icedata is a utility library that downloads and prepares computer vision datasets. We do not host or distribute these datasets, vouch for their quality or fairness, or claim that you have a license to use the dataset. It is your responsibility to determine whether you have permission to use the dataset under the its license.

If you are a dataset owner and wish to update any of the information in IceData (description, citation, etc.), or do not want your dataset to be included, please get in touch through a [GitHub issue](https://github.com/airctic/icedata/issues). Thanks for your contribution to the ML community!

If you are interested in learning more about responsible AI practices, including fairness, please see [Google AI's Responsible AI Practices](https://ai.google/responsibilities/responsible-ai-practices/).
