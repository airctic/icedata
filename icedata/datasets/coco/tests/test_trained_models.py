import pytest
import icedata
import torch.nn as nn


@pytest.mark.parametrize("model_name", icedata.coco.trained_models.__all__)
def test_trained_models(model_name):
    model_fn = getattr(icedata.coco.trained_models, model_name)
    model = model_fn()
    assert isinstance(model, nn.Module)
