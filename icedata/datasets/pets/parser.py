__all__ = ["parser", "PetsXmlParser", "PetsMaskParser", "PetsMaskFile"]

from icevision.imports import *
from icevision.core import *
from icevision import parsers


def parser(data_dir: Path, class_map: ClassMap, mask=False):
    annotations_dir = data_dir / "annotations/xmls"
    images_dir = data_dir / "images"
    masks_dir = data_dir / "annotations/trimaps"

    if not mask:
        parser = PetsXmlParser(
            annotations_dir=annotations_dir,
            images_dir=images_dir,
            class_map=class_map,
        )

    else:
        parser = PetsMaskParser(
            annotations_dir=annotations_dir,
            images_dir=images_dir,
            masks_dir=masks_dir,
            class_map=class_map,
        )

    return parser


class PetsXmlParser(parsers.VocXmlParser):
    def labels(self, o) -> List[Hashable]:
        name = re.findall(r"^(.*)_\d+$", o.stem)[0]

        # there is an image with two cats (same breed)
        num_objs = len(self._root.findall("object"))

        return [name] * num_objs


class PetsMaskParser(parsers.VocMaskParser, PetsXmlParser):
    def masks(self, o) -> List[Mask]:
        mask_file = self._imageid2maskfile[self.imageid(o)]
        return [PetsMaskFile(mask_file)]


class PetsMaskFile(VocMaskFile):
    """Extension of `MaskFile` for Pets masks.
    Invert 0s and 1s in the mask (the background is orignally 1 in the pets masks)
    Removes the color pallete and optionally drops void pixels.

    Args:
          drop_void (bool): drops the void pixels, which should have the value 255.
    """

    def to_mask(self, h, w) -> MaskArray:
        mask = super().to_mask(h=h, w=w)
        mask.data = 1 - mask.data
        return mask
