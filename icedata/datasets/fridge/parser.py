__all__ = ["parser", "dataset"]

from icevision.all import *


def parser(data_dir: Path):
    parser = parsers.VocXmlParser(
        annotations_dir=data_dir / "odFridgeObjects/annotations",
        images_dir=data_dir / "odFridgeObjects/images",
        class_map=ClassMap(["milk_bottle", "carton", "can", "water_bottle"]),
    )

    return parser


def dataset(
    data_dir: Path,
    size: int = 384,
    presize: int = 512,
    data_splitter: Optional[DataSplitter] = None,
):
    _parser = parser(data_dir=data_dir)

    train_records, valid_records = _parser.parse(data_splitter=data_splitter)

    train_tfms = tfms.A.Adapter(
        [*tfms.A.aug_tfms(size=size, presize=presize), tfms.A.Normalize()]
    )
    valid_tfms = tfms.A.Adapter([*tfms.A.resize_and_pad(size), tfms.A.Normalize()])

    train_ds = Dataset(train_records, train_tfms)
    valid_ds = Dataset(valid_records, valid_tfms)

    return train_ds, valid_ds