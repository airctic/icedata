__all__ = ["dataset"]

from icevision.all import *
from torch.utils import data
from icedata.datasets.exdark.parser import *
import icevision.tfms as tfms


def dataset(
    data_dir: Path,
    size: int = 384,
    presize: int = 512,
    data_splitter: Optional[DataSplitter] = None,
) -> Tuple[Dataset, Dataset]:

    _parser = parser(data_dir=data_dir)

    train_records, valid_records = _parser.parse(data_splitter=data_splitter)
    train_tfms = tfms.A.Adapter(
        [
            *tfms.A.aug_tfms(size=size, presize=presize, lightning=None),
            tfms.A.Normalize(),
        ]
    )
    valid_tfms = tfms.A.Adapter([*tfms.A.resize_and_pad(size), tfms.A.Normalize()])

    train_ds = Dataset(train_records, tfm=train_tfms)
    valid_ds = Dataset(valid_records, valid_tfms)

    return train_ds, valid_ds
