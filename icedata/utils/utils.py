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
    url: Union[str, Path],
    name: Union[str, Path],
    force_download: bool = False,
    dest_dir: Union[str, Path] = None,
    gdrive: bool = False,
) -> Path:
    if not dest_dir:
        dest_dir = get_data_dir()

    dest_dir = Path(dest_dir) / name
    if not dest_dir.exists() or force_download:
        dest_dir.mkdir(exist_ok=True, parents=True)
        save_path = dest_dir / Path(url).name
        if gdrive:
            download_and_extract_gdrive(url=url, extract_dir=save_path.parent)
        else:
            download_and_extract(url=url, save_path=save_path)

    return dest_dir
