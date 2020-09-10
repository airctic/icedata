import pytest
import icedata


@pytest.mark.parametrize("model_name", icedata.fridge.trained_models.__all__)
def test_trained_models(model_name):
    model_fn = getattr(icedata.fridge.trained_models, model_name)
    model = model_fn()
