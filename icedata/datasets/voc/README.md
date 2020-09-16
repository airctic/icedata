## Name
[**PASCAL VOC 2012 Dataset**](http://host.robots.ox.ac.uk/pascal/VOC/)

## Description
This dataset contains the data from the PASCAL Visual Object Classes Challenge 2012, a.k.a. VOC2012, corresponding to the Classification and Detection competitions. A total of 11540 images are included in this dataset, where each image contains a set of objects, out of 20 different classes, making a total of 27450 annotated objects.

**20 classes:**

- Person: person
- Animal: bird, cat, cow, dog, horse, sheep
- Vehicle: aeroplane, bicycle, boat, bus, car, motorbike, train
- Indoor: bottle, chair, dining table, potted plant, sofa, tv/monitor

## Annotations Examples
![image](images/voc_annotations.png)

## Usage 
<a href="https://colab.research.google.com/github/airctic/icevision/blob/master/notebooks/how_train_dataset.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> Example showing a dataset using the voc parser


## How to load this dataset
```python
# Imports
from icevision.all import *
import icedata

# Load the Pascal VOC dataset
path = icedata.voc.load_data()
```

## How to parse this dataset
```python
# Get the class_map, a utility that maps from number IDs to classs names
class_map = icedata.voc.class_map()

# Randomly split our data into train/valid
data_splitter = RandomSplitter([0.8, 0.2])

# VOC parser: provided out-of-the-box
parser = icedata.voc.parser(data_dir=path, class_map=class_map)
train_records, valid_records = parser.parse(data_splitter)

# shows images with corresponding labels and boxes
show_records(train_records[:6], ncols=3, class_map=class_map, show=True)
```

## How to load the pretrained weights of this dataset
```python
class_map = icedata.voc.class_map()
model = icedata.voc.trained_models.faster_rcnn_resnet50_fpn()
```

## Dataset folders
![image](images/voc_folders.png)

## Annotations sample
```xml
<annotation>
	<folder>VOC2012</folder>
	<filename>2007_000027.jpg</filename>
	<source>
		<database>The VOC2007 Database</database>
		<annotation>PASCAL VOC2007</annotation>
		<image>flickr</image>
	</source>
	<size>
		<width>486</width>
		<height>500</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>person</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>174</xmin>
			<ymin>101</ymin>
			<xmax>349</xmax>
			<ymax>351</ymax>
		</bndbox>
		<part>
			<name>head</name>
			<bndbox>
				<xmin>169</xmin>
				<ymin>104</ymin>
				<xmax>209</xmax>
				<ymax>146</ymax>
			</bndbox>
		</part>
		<part>
			<name>hand</name>
			<bndbox>
				<xmin>278</xmin>
				<ymin>210</ymin>
				<xmax>297</xmax>
				<ymax>233</ymax>
			</bndbox>
		</part>
		<part>
			<name>foot</name>
			<bndbox>
				<xmin>273</xmin>
				<ymin>333</ymin>
				<xmax>297</xmax>
				<ymax>354</ymax>
			</bndbox>
		</part>
		<part>
			<name>foot</name>
			<bndbox>
				<xmin>319</xmin>
				<ymin>307</ymin>
				<xmax>340</xmax>
				<ymax>326</ymax>
			</bndbox>
		</part>
	</object>
</annotation>
```

## License
Please check out [here](http://host.robots.ox.ac.uk/pascal/VOC/)

## Relevant Publications
[The PASCAL Visual Object Classes Challenge 2012 (VOC2012) Results](http://www.pascal-network.org/challenges/VOC/voc2012/workshop/index.html)

Everingham, M. and Van~Gool, L. and Williams, C. K. I. and Winn, J. and Zisserman, A.
