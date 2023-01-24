from icevision.imports import *
from icevision.utils import *
from icevision.core import *


def load_data(force_download=False) -> Path:
    """
    Downloads a trimmed version of the ExDark Dataset to "~/.icevision/data/exdark-trimmed"
    and returns the path it was downloaded to.

    Args:
        force_download (bool, optional): Defaults to False.

    Returns:
        Path: Path to load the dataset from
    """
    base_url = "https://github.com/ai-fast-track/icedata/releases/download/datasets/ExDark-Trimmed.zip"
    save_dir = get_data_dir() / "exdark-trimmed"
    save_dir.mkdir(exist_ok=True)

    save_path = save_dir / "exdark-trimmed.zip"
    if not save_path.exists() or force_download:
        download_and_extract(url=base_url, save_path=save_path)

    return save_dir / "ExDark-Trimmed"
