from icevision.imports import *
from icevision.utils import *
from icevision.core import *


def load_data(force_download=False):
    base_url = "https://github.com/ai-fast-track/icedata/releases/download/datasets/ExDark-Trimmed.zip"
    save_dir = get_data_dir() / "exdark-trimmed"
    save_dir.mkdir(exist_ok=True)

    save_path = save_dir / "exdark-trimmed.zip"
    if not save_path.exists() or force_download:
        download_and_extract(url=base_url, save_path=save_path)

    return save_dir
