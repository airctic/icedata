__all__ = ["parser"]

from icevision.imports import *
from icevision.core import *
from icevision import parsers


def parser(data_dir: Path):
    parser = parsers.VocXmlParser(
        annotations_dir=data_dir / "odFridgeObjects/annotations",
        images_dir=data_dir / "odFridgeObjects/images",
    )

    return parser
