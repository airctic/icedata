__all__ = ["parser", "BirdsParser", "BirdMaskFile"]

from icevision.imports import *
from icevision.utils import *
from icevision.core import *
from icevision.parsers import Parser


def parser(data_dir: Union[str, Path], class_map: ClassMap) -> Parser:
    return BirdsParser(data_dir=data_dir, class_map=class_map)


class BirdsParser(Parser):
    def __init__(self, data_dir, class_map):
        raise NotImplementedError("Has to be refactored to new API")
        self.mat_filepaths = get_files(
            data_dir / "annotations-mat", extensions=[".mat"]
        )
        self.class_map = class_map

    def __iter__(self) -> Any:
        yield from self.mat_filepaths

    def __len__(self) -> int:
        return len(self.mat_filepaths)

    def filepath(self, o) -> Union[str, Path]:
        parts = list(o.parts)
        parts[-3] = "images"
        return Path(*parts).with_suffix(".jpg")

    def imageid(self, o) -> Hashable:
        return o.stem

    def image_width_height(self, o) -> Tuple[int, int]:
        return get_image_size(self.filepath(o))

    def masks(self, o) -> List[Mask]:
        return [BirdMaskFile(o)]

    def bboxes(self, o) -> List[BBox]:
        import scipy.io

        mat = scipy.io.loadmat(str(o))
        bbox = mat["bbox"]
        xyxy = [int(bbox[pos]) for pos in ["left", "top", "right", "bottom"]]
        return [BBox.from_xyxy(*xyxy)]

    def labels(self, o) -> List[Hashable]:
        class_name = o.parent.name
        return [self.class_map.get_name(class_name)]


class BirdMaskFile(MaskFile):
    def to_mask(self, h, w):
        import scipy.io

        mat = scipy.io.loadmat(str(self.filepath))
        return MaskArray(mat["seg"])[None]
