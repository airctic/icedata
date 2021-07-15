__all__ = ["parser", "BirdsParser", "BirdMaskFile"]

from icevision.imports import *
from icevision.utils import *
from icevision.core import *
from icevision.parsers import Parser
from icedata.datasets.birds.data import class_map as class_map_fn


def parser(data_dir: Union[str, Path], class_map: Optional[ClassMap] = None) -> Parser:
    return BirdsParser(data_dir=data_dir, class_map=class_map)


class BirdsParser(Parser):
    def __init__(self, data_dir, class_map: Optional[ClassMap] = None):
        self.class_map = class_map or class_map_fn(data_dir)

        self.mat_filepaths = get_files(
            data_dir / "annotations-mat", extensions=[".mat"]
        )

        super().__init__(template_record=self.template_record())

    def __iter__(self) -> Any:
        yield from self.mat_filepaths

    def __len__(self) -> int:
        return len(self.mat_filepaths)

    def template_record(self) -> BaseRecord:
        return InstanceSegmentationRecord()

    def record_id(self, o) -> Hashable:
        return o.stem

    def parse_fields(self, o, record: BaseRecord, is_new: bool) -> None:
        if is_new:
            record.set_filepath(self.filepath(o))
            record.set_img_size(self.image_width_height(o))
            record.detection.set_class_map(self.class_map)

        record.detection.add_labels(self.labels(o))
        record.detection.add_bboxes(self.bboxes(o))
        record.detection.add_masks(self.masks(o))

    def filepath(self, o) -> Union[str, Path]:
        parts = list(o.parts)
        parts[-3] = "images"
        return Path(*parts).with_suffix(".jpg")

    def image_width_height(self, o) -> Tuple[int, int]:
        return get_img_size(self.filepath(o))

    def masks(self, o) -> List[Mask]:
        return [BirdMaskFile(o)]

    def bboxes(self, o) -> List[BBox]:
        import scipy.io

        mat = scipy.io.loadmat(str(o))
        bbox = mat["bbox"]
        xyxy = [int(bbox[pos]) for pos in ["left", "top", "right", "bottom"]]
        return [BBox.from_xyxy(*xyxy)]

    def labels(self, o) -> List[Hashable]:
        return [o.parent.name]
        # class_name = o.parent.name
        # return [self.class_map.get_name(class_name)]


class BirdMaskFile(MaskFile):
    def to_mask(self, h, w):
        import scipy.io

        mat = scipy.io.loadmat(str(self.filepath))
        return MaskArray(mat["seg"])[None]
