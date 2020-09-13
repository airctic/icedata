## Where can I get some help?
- If you find a bug, or you would like to suggest some new features, please file an issue [here](https://github.com/airctic/icedata/issues)

- If you need any assistance during your learning journey, feel free to join our [forum](https://spectrum.chat/mantis).


## How to install icedata?
To install the icedata package as well as all its dependencies, choose one of the 2 options:

Installing the icedata lastest version

```bash
pip install git+git://github.com/airctic/icedata.git#egg=icedata --upgrade
```

Install the icedata lastest version from Pypi repository:
```bash
pip install icedata
```

For more options, and more in-depth explanation on how to install icedata, please check out our [Installation Guide](https://airctic.github.io/icedata/install/
) 


## How to save trained weights in Google Colab?
In the following example, we show how to save trained weight using an EffecientDet model. The latter can be replaced by any model supported by icedata

Check out the [Train a Dataset Notebook](https://airctic.github.io/icedata/how_train_dataset/) to get familiar with all the steps from the training a dataset to saving the trained weights. 

```python
# Model
model = efficientdet.model(
    model_name="tf_efficientdet_lite0", num_classes=len(class_map), img_size=size
)
# Train the model using either Fastai Learner of Pytorch-Lightning Trainer

## Saving a Model on Google Drive
from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)
root_dir = Path('/content/gdrive/My Drive/')

torch.save(model.state_dict(), root_dir/'icedata/models/fridge/fridge_tf_efficientdet_lite0.pth')
```

## How to load pretrained weights?
In this example, we show how to create a Faster RCNN model, and load pretrained weight that were previously obtained during the training of the PETS dataset as shown in the [Getting Started Notebook](https://airctic.github.io/icevision/getting_started/)

```python
# Maps IDs to class names.
class_map = datasets.pets.class_map()

# Model trained in `Tutorials->Getting Started`
WEIGHTS_URL = "https://github.com/airctic/model_zoo/releases/download/pets_faster_resnet50fpn/pets_faster_resnetfpn50.zip"

# Create the same model used in training and load the weights
# `map_location` will put the model on cpu, optionally move to gpu if necessary
model = faster_rcnn.model(num_classes=len(class_map))
state_dict = torch.hub.load_state_dict_from_url(
    WEIGHTS_URL, map_location=torch.device("cpu")
)
model.load_state_dict(state_dict)
```

## How to contribute?
We are both a welcoming and an open community. We warmly invite you to join us either as a user or a community contributor. We will be happy to hear from you.

To contribute, please follow the [Contributing Guide](https://airctic.github.io/icedata/contributing/). 
