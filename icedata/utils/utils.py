__all__ = ["load_model_weights_from_url", "load_data"]

from icevision.all import *


def load_model_weights_from_url(
    model: nn.Module, url: str, map_location=torch.device("cpu"), **kwargs
) -> None:
    state_dict = torch.hub.load_state_dict_from_url(
        url, map_location=map_location, **kwargs
    )
    model.load_state_dict(state_dict)


def load_data(
    url: Union[str, Path], name: Union[str, Path], force_download: bool = False
) -> Path:
    save_dir = get_data_dir() / name
    save_dir.mkdir(exist_ok=True)

    if not save_dir.exists() or force_download:
        save_path = save_dir / Path(url).name
        download_and_extract(url=url, save_path=save_path)

    return save_dir
