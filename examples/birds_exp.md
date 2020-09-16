# How to use the Birds dataset

```python
# Imports
from icevision.all import *
import icedata

# Load the Birds dataset
path = icedata.birds.load_data()

# Get the class_map, a utility that maps from number IDs to classs names
class_map = icedata.birds.class_map()

# Randomly split our data into train/valid
data_splitter = RandomSplitter([0.8, 0.2])

# Birds parser: provided out-of-the-box
parser = icedata.birds.parser(data_dir=path, class_map=class_map)
train_records, valid_records = parser.parse(data_splitter)

# shows images with corresponding labels and boxes
show_records(train_records[:6], ncols=3, class_map=class_map, show=True)

# load the pretrained model
model = icedata.birds.trained_models.faster_rcnn_resnet50_fpn()
```
