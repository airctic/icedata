__all__ = ["tf_efficientdet_lite0", "faster_rcnn_resnet50_fpn"]

from icevision.all import *
from icedata.utils import load_model_weights_from_url
from icedata.datasets.fridge.data import NUM_CLASSES


def _load_efficientdet(name, weights_url):
    model = efficientdet.model(name, num_classes=NUM_CLASSES, img_size=512)
    load_model_weights_from_url(model, weights_url)
    return model


def _load_faster_rcnn(backbone, weights_url):
    model = faster_rcnn.model(num_classes=NUM_CLASSES, backbone=backbone)
    load_model_weights_from_url(model=model, url=weights_url)
    return model


def tf_efficientdet_lite0():
    weights_url = "https://github.com/airctic/model_zoo/releases/download/m2/fridge_tf_efficientdet_lite0.zip"
    return _load_efficientdet("tf_efficientdet_lite0", weights_url)


def faster_rcnn_resnet50_fpn():
    weights_url = "https://github.com/airctic/model_zoo/releases/download/m1/fridge_faster_resnetfpn50.zip"
    return _load_faster_rcnn(None, weights_url)
