## Name 
**My Awesome Dataset**

## Description
Describe your dataset.

## Annotations Examples
<!-- Please add an image showing an sample image with its annotation -->
![image](images/my_awesome_dataset.png)

## Usage 
<!-- Please replace my_awesome_dataset by the name of your notebook -->
<a href="https://colab.research.google.com/github/airctic/icedata/blob/master/notebooks/dev/my_awesome_dataset.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> Example showing how to use this dataset


## How to load this dataset
```python
# Imports
from icevision.all import *
import icedata

# Load the Fridge Objects dataset
path = icedata.my_awesome_dataset.load_data()
```

## How to parse this dataset
```python
# Get the class_map, a utility that maps from number IDs to classs names
class_map = icedata.my_awesome_dataset.class_map()

# Randomly split our data into train/valid
data_splitter = RandomSplitter([0.8, 0.2])

# Fridge parser: provided out-of-the-box
parser = icedata.my_awesome_dataset.parser(data_dir=path, class_map=class_map)
train_records, valid_records = parser.parse(data_splitter)

# shows images with corresponding labels and boxes
show_records(train_records[:6], ncols=3, class_map=class_map, show=True)
```

## How to load the pretrained weights of this dataset
```python
class_map = icedata.my_awesome_dataset.class_map()
model = icedata.my_awesome_dataset.trained_models.faster_rcnn_resnet50_fpn()
```

## Dataset folders
![image](images/my_awesome_dataset_folders.png)

## Annotations sample
<!-- Please replace this annotation sample by one extracted from my_awesome_dataset -->

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
<!-- Please add the my_awesome_dataset license here -->
Unknown

## Relevant Publications
<!-- Please add the my_awesome_dataset publications here -->
[My Awesome Dataset Paper](https://arxiv.org/abs/???)