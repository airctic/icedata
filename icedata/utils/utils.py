__all__ = ["load_model_weights_from_url"]

from icevision.all import *


def load_model_weights_from_url(
    model: nn.Module, url: str, map_location=torch.device("cpu"), **kwargs
) -> None:
    state_dict = torch.hub.load_state_dict_from_url(
        url, map_location=map_location, **kwargs
    )
    model.load_state_dict(state_dict)
