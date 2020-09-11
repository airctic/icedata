import pytest
import icedata


@pytest.mark.parametrize("model_name", icedata.pennfudan.trained_models.__all__)
def test_trained_models(model_name):
    model_fn = getattr(icedata.pennfudan.trained_models, model_name)
    model = model_fn()
