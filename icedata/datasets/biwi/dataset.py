__all__ = ["dataset"]

from icevision.all import *
from .parser import *


def dataset(
    data_dir: Path,
    size: int = 384,
    presize: int = 512,
    data_splitter: Optional[DataSplitter] = None,
):
    _parser = parser(data_dir=data_dir)

    train_records, valid_records = _parser.parse(data_splitter=data_splitter)

    train_tfms = tfms.A.Adapter(
        [*tfms.A.aug_tfms(size=size, presize=presize, crop_fn=None), tfms.A.Normalize()]
    )
    valid_tfms = tfms.A.Adapter([*tfms.A.resize_and_pad(size), tfms.A.Normalize()])

    train_ds = Dataset(train_records, train_tfms)
    valid_ds = Dataset(valid_records, valid_tfms)

    return train_ds, valid_ds
