__all__ = ["parser"]

from icevision.all import *

_COLOR_MAP = {
    "milk_bottle": "#1542e2",
    "carton": "#10a530",
    "can": "#f03923",
    "water_bottle": "#e2d430",
}


def parser(data_dir: Path):
    parser = parsers.VOCBBoxParser(
        annotations_dir=data_dir / "odFridgeObjects/annotations",
        images_dir=data_dir / "odFridgeObjects/images",
        class_map=ClassMap(
            ["milk_bottle", "carton", "can", "water_bottle"],
            color_map=_COLOR_MAP,
        ),
    )

    return parser
