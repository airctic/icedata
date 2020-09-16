## Name
[**COCO Dataset**](https://cocodataset.org/#home)

## Description
COCO is a large-scale object detection, segmentation, and captioning dataset. COCO has several features:

- Object segmentation

- Recognition in context

- Superpixel stuff segmentation

- 330K images (>200K labeled)

- 1.5 million object instances

- 80 object categories

- 91 stuff categories

- 5 captions per image

- 250,000 people with keypoint

## Annotations Examples
![image](images/coco_annotations.jpg)


## Usage 
A Colab notebook will be added


## How to load this dataset
```python
# Imports
from icevision.all import *
import icedata

# Load the COCO dataset
path = icedata.coco.load_data()
```

## How to parse this dataset
```python
# Get the class_map, a utility that maps from number IDs to classs names
class_map = icedata.coco.class_map()

# Randomly split our data into train/valid
data_splitter = RandomSplitter([0.8, 0.2])

# COCO parser: provided out-of-the-box
parser = icedata.coco.parser(data_dir=path, class_map=class_map)
train_records, valid_records = parser.parse(data_splitter)

# shows images with corresponding labels and boxes
show_records(train_records[:6], ncols=3, class_map=class_map, show=True)
```

## How to load the pretrained weights of this dataset
```python
class_map = icedata.coco.class_map()
model = icedata.coco.trained_models.faster_rcnn_resnet50_fpn()
```

## Dataset folders
TODO

## Annotations Structure
**COCO Bounding box:** (x-top left, y-top left, width, height)

**Pascal VOC Bounding box** :(x-top left, y-top left,x-bottom right, y-bottom right)

COCO has several annotation types: for object detection, keypoint detection, stuff segmentation, panoptic segmentation, densepose, and image captioning. The annotations are stored using JSON. Please note that the COCO API described on the download page can be used to access and manipulate all anotations. All annotations share the same basic data structure below:
```json
{
    "info": info, 
    "images": [image], 
    "annotations": [annotation], 
    "licenses": [license],
}

info{
    "year": int, 
    "version": str, 
    "description": str, 
    "contributor": str, 
    "url": str, 
    "date_created": datetime,
}

image{
    "id": int, 
    "width": int, 
    "height": int, 
    "file_name": str, 
    "license": int, 
    "flickr_url": str, 
    "coco_url": str, 
    "date_captured": datetime,
}

license{
    "id": int, 
    "name": str, 
    "url": str,
}
```

The data structures specific to the object detection annotation types is described below.
### Object Detection Annotation
Each object instance annotation contains a series of fields, including the category id and segmentation mask of the object. The segmentation format depends on whether the instance represents a single object (iscrowd=0 in which case polygons are used) or a collection of objects (iscrowd=1 in which case RLE is used). Note that a single object (iscrowd=0) may require multiple polygons, for example if occluded. Crowd annotations (iscrowd=1) are used to label large groups of objects (e.g. a crowd of people). In addition, an enclosing bounding box is provided for each object (box coordinates are measured from the top left image corner and are 0-indexed). Finally, the categories field of the annotation structure stores the mapping of category id to category and supercategory names. See also the detection task.

```json
annotation{
    "id": int, 
    "image_id": int, 
    "category_id": int, 
    "segmentation": RLE or [polygon], 
    "area": float, 
    "bbox": [x,y,width,height], 
    "iscrowd": 0 or 1,
}

categories[{
    "id": int, 
    "name": str, 
    "supercategory": str,
}]
```

## License
The dataset is available to download for commercial/research purposes under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/). The copyright remains with the original owners of the images.

## Relevant Publications
[Microsoft COCO: Common Objects in Context](https://arxiv.org/abs/1405.0312v3)

Tsung-Yi Lin, Michael Maire, Serge Belongie, Lubomir Bourdev, Ross Girshick, James Hays, Pietro Perona, Deva Ramanan, C. Lawrence Zitnick, Piotr Dollár
