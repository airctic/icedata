import pytest
import icedata
import torch.nn as nn


@pytest.mark.parametrize("model_name", icedata.TK_DATASET_NAME.trained_models.__all__)
def test_trained_models(model_name):
    model_fn = getattr(icedata.TK_DATASET_NAME.trained_models, model_name)
    model = model_fn()
    assert isinstance(model, nn.Module)
