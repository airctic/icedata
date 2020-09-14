## Name
[**The Oxford-IIIT Pet Dataset**](https://www.robots.ox.ac.uk/~vgg/data/pets/)

## Description
Pet dataset has 37 classes roughly 200 images for each class. The images have a large variations in scale, pose and lighting. All images have an associated ground truth annotation of breed, head ROI, and pixel level trimap segmentation.

## Annotations Examples
![image](images/pet_annotations.jpg)

## Usage 
<a href="https://colab.research.google.com/github/airctic/icevision/blob/master/notebooks/getting_started.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> Example showing how to use this dataset


## How to load this dataset
```python
# Imports
from icevision.all import *
import icedata

# Load the PETS dataset
path = icedata.pets.load_data()
```

## How to parse this dataset
```python
# Get the class_map, a utility that maps from number IDs to classs names
class_map = icedata.pets.class_map()

# Randomly split our data into train/valid
data_splitter = RandomSplitter([0.8, 0.2])

# PETS parser: provided out-of-the-box
parser = icedata.pets.parser(data_dir=path, class_map=class_map)
train_records, valid_records = parser.parse(data_splitter)

# shows images with corresponding labels and boxes
show_records(train_records[:6], ncols=3, class_map=class_map, show=True)
```

## How to load the pretrained weights of this dataset
```python
class_map = icedata.pets.class_map()
model = icedata.pets.trained_models.faster_rcnn_resnet50_fpn()
```

## Dataset folders
![image](images/pets_folders.png)

## Annotations sample
```xml
<annotation>
    <folder>OXIIIT</folder>
    <filename>Abyssinian_1.jpg</filename>
    <source>
        <database>OXFORD-IIIT Pet Dataset</database>
        <annotation>OXIIIT</annotation>
        <image>flickr</image>
    </source>
    <size>
        <width>600</width>
        <height>400</height>
        <depth>3</depth>
    </size>
    <segmented>0</segmented>
    <object>
        <name>cat</name>
        <pose>Frontal</pose>
        <truncated>0</truncated>
        <occluded>0</occluded>
        <bndbox>
            <xmin>333</xmin>
            <ymin>72</ymin>
            <xmax>425</xmax>
            <ymax>158</ymax>
        </bndbox>
        <difficult>0</difficult>
    </object>
</annotation>
```

## License
The dataset is available to download for commercial/research purposes under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). The copyright remains with the original owners of the images.

## Relevant Publications
Cats and Dogs

O. M. Parkhi, A. Vedaldi, A. Zisserman, C. V. Jawahar

IEEE Conference on Computer Vision and Pattern Recognition, 2012