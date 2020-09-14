import pytest
import icedata
import torch.nn as nn


@pytest.mark.parametrize("model_name", icedata.pennfudan.trained_models.__all__)
def test_trained_models(model_name) -> nn.Module:
    model_fn = getattr(icedata.pennfudan.trained_models, model_name)
    model = model_fn()
    assert isinstance(model, nn.Module)
