<div align="center">
  <img src="images/icedata-logo-slogan.png" alt="logo" width="400px" style="display: block; margin-left: auto; margin-right: auto"/>
  <h2><b>Datasets Hub for the IceVision Framework</b></h2>
</div>

* * * * *
>**Note: "We Need Your Help"**
    If you find this work useful, please let other people know by **starring** it,
    and sharing it. 
    Thank you!
    
<div align="center">
  
[![tests](https://github.com/airctic/icedata/workflows/tests/badge.svg?event=push)](https://github.com/airctic/icedata/actions?query=workflow%3Atests)
[![docs](https://github.com/airctic/icedata/workflows/docs/badge.svg)](https://airctic.github.io/icedata/)
[![codecov](https://codecov.io/gh/airctic/icedata/branch/master/graph/badge.svg)](https://codecov.io/gh/airctic/icedata)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/airctic/icevision/blob/master/LICENSE)  

[![Join Users Forum](https://withspectrum.github.io/badge/badge.svg)](https://spectrum.chat/mantis)

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

For more installation options, check our [docs](https://airctic.github.io/icevdata/install/).

**Important:** We currently only support Linux/MacOS.
<!-- Not included in docs - end -->

## Why IceData?

- IceData is Datasets Hub for our [IceVision](https://github.com/airctic/icevision) Framework

- Uses the IceVision Unified Data API with out-of-the-box support for common annotation formats (COCO, VOC, etc.)

- It hosts community maintained parsers and custom datasets 

- Provides a nice overview of each hosted dataset including a description, an annotation example, and some other relevant information

- Make end-to-end training using thoses datasets a very straightforward process through code reuse thanks to its unified API

- Enables practioners to get moving with object detection technology quickly



## Datasets

[**Source**](https://github.com/airctic/icedata/tree/master/icedata/datasets)


`Datasets` are designed to simplify both loading and parsing a wide range of computer vision datasets.

**Main Features:**

- Smart Caching: We cache the data so no need to re-download it.

- Lightweight and fast with a transparent and pythonic API.

- Out-of-the-box parsers to convert different datasets into IceVision Data Format.

IceData provides several ready-to-use datasets that use both standard annotation format such as COCO and VOC as well as custom annotation formats such [WheatParser](https://airctic.github.io/icevision/custom_parser/) used in the [Kaggle Global Wheat Competition](https://www.kaggle.com/c/global-wheat-detection) 


## Usage

Object detection datasets use different annotations formats (COCO, VOC, and custom formats). IceVision offers different options to parse each one of those formats:


## Case 1: COCO, and VOC compatible datasets

### **Option 1: Using icevision predefined VOC parser**
**Example:** Raccoon - dataset using the predefined VOC parser

```python
# Imports
from icevision.all import *
import icedata


# WARNING: Make sure you have already cloned the raccoon dataset using the command shown here above
# Set images and annotations directories
data_dir = Path("raccoon_dataset")
images_dir = data_dir / "images"
annotations_dir = data_dir / "annotations"

# Define class_map
class_map = ClassMap(["raccoon"])

# Parser: Use icevision predefined VOC parser
parser = parsers.voc(
    annotations_dir=annotations_dir, images_dir=images_dir, class_map=class_map
)

# train and validation records
train_records, valid_records = parser.parse()
show_records(train_records[:3], ncols=3, class_map=class_map)
```

!!! info "Note" 
    Notice how we use the predifined [parsers.voc()](https://github.com/airctic/icevision/blob/master/icevision/parsers/voc_parser.py) function:
    
    **parser = parsers.voc(
    annotations_dir=annotations_dir, images_dir=images_dir, class_map=class_map
    )**


### **Option 2: Creating both data, and parsers files for the VOC or COCO parsers**

**Example:** Fridge Objects - dataset redefining its VOC parser

Please check out the [fridge folder](https://github.com/airctic/icedata/tree/master/icedata/datasets/fridge) for more information on how this dataset is structured.

```python
# Imports
from icevision.all import *
import icedata

# Load the Fridge Objects dataset
data_dir = icedata.fridge.load()

# Get the class_map, a utility that maps from number IDs to classs names
class_map = icedata.fridge.class_map()

# VOC parser: provided out-of-the-box
parser = icedata.fridge.parser(data_dir, class_map)
train_records, valid_records = parser.parse()

# shows images with corresponding labels and boxes
show_records(train_records[:3], ncols=3, class_map=class_map)
```

!!! info "Note" 
    Notice how we use a new defined [icedata.fridge.parser()](https://github.com/airctic/icedata/blob/master/icedata/datasets/fridge/parsers.py) function:
    
    **parser = icedata.fridge.parser(data_dir, class_map)**


## Case 2: Dataset using a custom parser

**Example:** PETS - a dataset using its custom parser

Please check out the [pets folder](https://github.com/airctic/icedata/tree/master/icedata/datasets/pets) for more information on how this dataset is structured.

```python
# Imports
from icevision.all import *
import icedata

# Load the PETS dataset
path = icedata.pets.load()

# Get the class_map, a utility that maps from number IDs to classs names
class_map = icedata.pets.class_map()

# PETS parser: provided out-of-the-box
parser = icedata.pets.parser(data_dir=path, class_map=class_map)
train_records, valid_records = parser.parse()

# shows images with corresponding labels and boxes
show_records(train_records[:6], ncols=3, class_map=class_map, show=True)

```

!!! info "Note 1" 
    The datasets interface will always have at least the following functions: [load](https://github.com/airctic/icedata/blob/master/icedata/datasets/pets/data.py), [class_map](https://github.com/airctic/icedata/blob/master/icedata/datasets/pets/data.py), and [parser](https://github.com/airctic/icedata/blob/master/icedata/datasets/pets/parsers.py). You might also have noticed the strong similarity between the 2 examples listed here above. Indeed, only the names of the datasets differ, the rest of the code is the same: That highlights how we both simpified and standardized the process of loading and parsing a given dataset.

!!! info "Note 2" 
    If you would like to create your own dataset, we strongly recommend you following the same file structure, and naming found in the different examples such as the [Fridge Objects dataset](https://github.com/airctic/icedata/tree/master/icedata/datasets/fridge), and the [PETS dataset](https://github.com/airctic/icedata/tree/master/icedata/datasets/pets)    

![image](https://airctic.github.io/icedata/images/datasets-folder-structure.png)

# Disclaimer

Inspired from the excellent HuggingFace [nlp](https://github.com/huggingface/nlp) project, icedata is a utility library that downloads and prepares computer vision datasets. We do not host or distribute these datasets, vouch for their quality or fairness, or claim that you have license to use the dataset. It is your responsibility to determine whether you have permission to use the dataset under the dataset's license.

If you are a dataset owner and wish to update any part of it (description, citation, etc.), or do not want your dataset to be included in this library, please get in touch through a [GitHub issue](https://github.com/airctic/icedata/issues). Thanks for your contribution to the ML community!

If you are interested in learning more about responsible AI practices, including fairness, please see [Google AI's Responsible AI Practices](https://ai.google/responsibilities/responsible-ai-practices/).
