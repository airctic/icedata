## Name 
**Fridge Objects Dataset**

## Description
Fridge Objects is a toy dataset which consists of 134 images with 4 classes of beverage container {can, carton, milk bottle, water bottle} pictures taken on different backgrounds.

## Annotations Examples
![image](images/fridge_annotations.png)

## Usage 
<a href="https://colab.research.google.com/github/airctic/icevision/blob/master/notebooks/how_train_dataset.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> Example showing how to use this dataset


## How to load this dataset
```python
# Imports
from icevision.all import *
import icedata

# Load the Fridge Objects dataset
path = icedata.fridge.load_data()
```

## How to parse this dataset
```python
# Get the class_map, a utility that maps from number IDs to classs names
class_map = icedata.fridge.class_map()

# Randomly split our data into train/valid
data_splitter = RandomSplitter([0.8, 0.2])

# Fridge parser: provided out-of-the-box
parser = icedata.fridge.parser(data_dir=path, class_map=class_map)
train_records, valid_records = parser.parse(data_splitter)

# shows images with corresponding labels and boxes
show_records(train_records[:6], ncols=3, class_map=class_map, show=True)
```

## How to load the pretrained weights of this dataset
```python
class_map = icedata.fridge.class_map()
model = icedata.fridge.trained_models.faster_rcnn_resnet50_fpn()
```

## Dataset folders
![image](images/fridge_folders.png)

## Annotations sample
```xml
<annotation>
	<folder>images</folder>
	<filename>2.jpg</filename>
	<path>../images/2.jpg</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>499</width>
		<height>666</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>milk_bottle</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>247</xmin>
			<ymin>192</ymin>
			<xmax>355</xmax>
			<ymax>493</ymax>
		</bndbox>
	</object>
</annotation>
```

## License
Unknown

## Relevant Publications
Unknown
