__all__ = ["faster_rcnn_resnet50_fpn"]

from icevision.all import *
from icedata.utils import load_model_weights_from_url
from icedata.datasets.coco.data import NUM_CLASSES


def faster_rcnn_resnet50_fpn() -> nn.Module:
    weights_url = (
        "https://download.pytorch.org/models/fasterrcnn_resnet50_fpn_coco-258fb6c6.pth"
    )
    model = faster_rcnn.model(num_classes=NUM_CLASSES)
    load_model_weights_from_url(model=model, url=weights_url)
    return model
