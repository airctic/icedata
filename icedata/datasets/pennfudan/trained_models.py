__all__ = ["mask_rcnn_resnet50_fpn"]

from warnings import warn

from icevision.all import *
from icedata.utils import load_model_weights_from_url
from icedata.datasets.pennfudan.data import NUM_CLASSES


def mask_rcnn_resnet50_fpn() -> nn.Module:
    warn(
        "Weights can currently not be loaded from state dict. This issue will be fixed in the future."
    )
    # weights_url = "https://github.com/airctic/icedata/releases/download/m1/pennfudan_maskrcnn_resnet50_fpn.zip"
    # weights_url = "https://github.com/airctic/model_zoo/releases/download/pennfudan_maskrcnn_resnet50fpn/pennfudan_maskrcnn_resnet50fpn.zip"
    model = models.torchvision.faster_rcnn.model(num_classes=NUM_CLASSES)
    # load_model_weights_from_url(model=model, url=weights_url)
    return model
