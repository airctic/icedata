__all__ = ["dataset"]

from icevision.all import *
from .parser import *


def dataset(
    data_dir: Path,
    size: int = 384,
    presize: int = 512,
    data_splitter: Optional[DataSplitter] = None,
    task: str = "bbox",
):
    if task == "bbbox":
        parser = parsers.COCOBBoxParser
    elif task == "mask":
        parser = parsers.COCOMaskParser
    elif task == "keypoints":
        parser = parsers.COCOKeyPointsParser
    else:
        raise ValueError(
            f"The 'task' argmument passed is '{task}'. 'task' argument must be one o these 3 values 'bbox', 'mask, or 'keypoints'. "
        )

    _parser = parser(
        annotations_file=data_dir / "annotations.json", img_dir=data_dir / "images"
    )

    train_records, valid_records = _parser.parse(data_splitter=data_splitter)

    train_tfms = tfms.A.Adapter(
        [*tfms.A.aug_tfms(size=size, presize=presize), tfms.A.Normalize()]
    )
    valid_tfms = tfms.A.Adapter([*tfms.A.resize_and_pad(size), tfms.A.Normalize()])

    train_ds = Dataset(train_records, train_tfms)
    valid_ds = Dataset(valid_records, valid_tfms)

    return train_ds, valid_ds
