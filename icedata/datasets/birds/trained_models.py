__all__ = ["mask_rcnn_resnet50_fpn"]

from icevision.all import *
from icedata.utils import load_model_weights_from_url
from icedata.datasets.birds.data import NUM_CLASSES


def mask_rcnn_resnet50_fpn() -> nn.Module:
    weights_url = "https://github.com/airctic/model_zoo/releases/download/m4/birds_maskrcnn_resnet50fpn.zip"
    model = mask_rcnn.model(num_classes=NUM_CLASSES)
    load_model_weights_from_url(model=model, url=weights_url)
    return model
