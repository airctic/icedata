__all__ = ["parser"]

from icevision.all import *


def parser(data_dir: Path):
    parser = parsers.VOCBBoxParser(
        annotations_dir=data_dir / "odFridgeObjects/annotations",
        images_dir=data_dir / "odFridgeObjects/images",
        class_map=ClassMap(["milk_bottle", "carton", "can", "water_bottle"]),
    )

    return parser
