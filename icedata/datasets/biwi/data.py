__all__ = ["NUM_CLASSES", "load_data"]

from icevision.imports import *
from icevision.core import *
from icevision.utils import *

NUM_CLASSES = 1 + 1


def load_data(force_download: bool = False):
    url = "https://s3.amazonaws.com/fast-ai-sample/biwi_sample.tgz"
    save_dir = get_data_dir() / "biwi"
    save_dir.mkdir(exist_ok=True)
    tar_file = save_dir / "biwi_sample.tgz"

    if not tar_file.exists() or force_download:
        download_and_extract(url=url, save_path=tar_file)

    return save_dir
