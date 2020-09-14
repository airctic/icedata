__all__ = ["NUM_CLASSES", "class_map", "load_data"]

from icevision.imports import *
from icevision.core import *

_CLASSES = [
    "person",
    "bicycle",
    "car",
    "motorcycle",
    "airplane",
    "bus",
    "train",
    "truck",
    "boat",
    "traffic light",
    "fire hydrant",
    "N/A",
    "stop sign",
    "parking meter",
    "bench",
    "bird",
    "cat",
    "dog",
    "horse",
    "sheep",
    "cow",
    "elephant",
    "bear",
    "zebra",
    "giraffe",
    "N/A",
    "backpack",
    "umbrella",
    "N/A",
    "N/A",
    "handbag",
    "tie",
    "suitcase",
    "frisbee",
    "skis",
    "snowboard",
    "sports ball",
    "kite",
    "baseball bat",
    "baseball glove",
    "skateboard",
    "surfboard",
    "tennis racket",
    "bottle",
    "N/A",
    "wine glass",
    "cup",
    "fork",
    "knife",
    "spoon",
    "bowl",
    "banana",
    "apple",
    "sandwich",
    "orange",
    "broccoli",
    "carrot",
    "hot dog",
    "pizza",
    "donut",
    "cake",
    "chair",
    "couch",
    "potted plant",
    "bed",
    "N/A",
    "dining table",
    "N/A",
    "N/A",
    "toilet",
    "N/A",
    "tv",
    "laptop",
    "mouse",
    "remote",
    "keyboard",
    "cell phone",
    "microwave",
    "oven",
    "toaster",
    "sink",
    "refrigerator",
    "N/A",
    "book",
    "clock",
    "vase",
    "scissors",
    "teddy bear",
    "hair drier",
    "toothbrush",
]

NUM_CLASSES = len(_CLASSES) + 1


def class_map(background: Optional[int] = 0) -> ClassMap:
    return ClassMap(classes=_CLASSES, background=background)


def load_data():
    raise NotImplementedError(
        "Downloading data for COCO is not implemented, please consider following the "
        "official instructions avaiable [here](https://cocodataset.org/#download) "
        "to download the dataset"
    )


# def class_map(annotations_file, background: Optional[int] = 0) -> ClassMap:
#     annotations_dict = json.loads(annotations_file.read())
#     classes = [cat["name"] for cat in annotations_dict["categories"]]
#     return ClassMap(classes=classes, background=background)
