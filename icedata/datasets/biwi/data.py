__all__ = ["load_data", "load"]

from icevision.imports import *
from icevision.core import *
from icevision.utils import *


def load_data(force_download: bool = False):
    url = "https://s3.amazonaws.com/fast-ai-sample/biwi_sample.tgz"
    save_dir = get_data_dir() / "biwi"
    save_dir.mkdir(exist_ok=True)
    tar_file = save_dir / "biwi_sample.tgz"

    if not tar_file.exists() or force_download:
        download_and_extract(url=url, save_path=tar_file)

    return save_dir


def load(force_download: bool = False):
    warnings.warn("load will be deprecated in 0.1.0, please use load_data instead")
    return load_data(force_download=force_download)
