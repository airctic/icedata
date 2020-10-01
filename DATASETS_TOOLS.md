# Datasets Tools
The goal is to gather some useful resources that will help both beginners and advanced users creating and/or processing their datasets. 


## Datasets repositories

[VisualData.io](https://www.visualdata.io/discovery): A search engine that references hundreds of datasets.

[Roboflow Datasets](https://public.roboflow.com/): Roboflow hosts free public computer vision datasets in many popular formats (including CreateML JSON, COCO JSON, Pascal VOC XML, YOLO v3, and Tensorflow TFRecords).

[Open Images](https://storage.googleapis.com/openimages/web/index.html): Huge dataset containing more than 1,700,000 images with related bounding boxes, and 600 classes.

## Datasets creation tools

[OIDv4 ToolKit](https://github.com/EscVM/OIDv4_ToolKit): Open Images Dataset v4 Toolkit. 
### Object Detection
* download any of the 600 classes of the dataset individually, taking care of creating the related bounding boxes for each downloaded image
* download multiple classes at the same time creating separated folder and bounding boxes for each of them
* download multiple classes and creating a common folder for all of them with a unique annotation file of each image
* download a single class or multiple classes with the desired attributes
* use the practical visualizer to inspect the donwloaded classes

### Image Classification

* download any classes in a common labeled folder
* exploit tens of possible commands to select only the desired images

## Useful tools such annotations tools

[Remo](https://github.com/rediscovery-io/remo-python):  a web-based application to organize, annotate and visualize Computer Vision datasets. Remo runs on Windows, Linux, Mac or directly in Google Colab Notebooks. It can also be served on a private server for team collaboration, or embedded in Jupyter Notebooks.

[VoTT (Visual Object Tagging Tool)](https://github.com/microsoft/VoTT): annotation and labeling tool for image and video assets. VoTT can be installed as a native application or run from source. VoTT is also available as a [stand-alone Web application](https://vott.z22.web.core.windows.net/#/) and can be used in any modern Web browser.