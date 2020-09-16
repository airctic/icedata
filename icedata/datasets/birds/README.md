## Name
[**Caltech-UCSD Birds 200 Dataset**](http://www.vision.caltech.edu/visipedia/CUB-200.html)

## Description
Caltech-UCSD Birds 200 (CUB-200) is an image dataset with photos of 200 bird species (mostly North American). For detailed information about the dataset, please see the technical report [^1] linked below.

- Number of categories: 200

- Number of images: 6,033

- Annotations: Bounding Box, Rough Segmentation, Attributes

## Annotations Examples
![image](images/birds_annotations.png)

## Usage 
A Colab notebook will be added


## How to load this dataset
```python
# Imports
from icevision.all import *
import icedata

# Load the Birds dataset
path = icedata.birds.load_data()
```

## How to parse this dataset
```python
# Get the class_map, a utility that maps from number IDs to classs names
class_map = icedata.birds.class_map()

# Randomly split our data into train/valid
data_splitter = RandomSplitter([0.8, 0.2])

# Birds parser: provided out-of-the-box
parser = icedata.birds.parser(data_dir=path, class_map=class_map)
train_records, valid_records = parser.parse(data_splitter)

# shows images with corresponding labels and boxes
show_records(train_records[:6], ncols=3, class_map=class_map, show=True)
```

## How to load the pretrained weights of this dataset
```python
class_map = icedata.birds.class_map()
model = icedata.birds.trained_models.faster_rcnn_resnet50_fpn()
```

## Dataset folders
For more information about the dataset, visit the project [website](http://www.vision.caltech.edu/visipedia)

**Directory Information**

- images/
    The images organized in subdirectories based on species.

- annotations-mat/
    Bounding box and rough segmentation annotations. Organized as
    the images.

- attributes/
    Attribute data from MTurk workers.

- attributes-yaml/
    Contains the same attribute data as in 'attributes/' but stored for each
    file as a yaml file with the same name as the image file.

- lists/
    classes.txt : list of categories (species)

    files.txt   : list of all image files (including subdirectories)

    train.txt   : list of all images used for training

    test.txt    : list of all images used for testing

    splits.mat  : training/testing splits in MATLAB .mat format

## Annotations sample
It uses MATLAB files. Check out the birds [AnnotationParser, BirdMaskFile](https://github.com/airctic/icedata/blob/master/icedata/datasets/birds/parsers.py) classes.

## License
Please check out [here](http://www.vision.caltech.edu/visipedia/CUB-200.html)

## Relevant Publications
[^1]:
    [Caltech-UCSD Birds 200](http://www.vision.caltech.edu/visipedia/papers/WelinderEtal10_CUB-200.pdf)

    Welinder P., Branson S., Mita T., Wah C., Schroff F., Belongie S., Perona, P. 

    California Institute of Technology. CNS-TR-2010-001. 2010
