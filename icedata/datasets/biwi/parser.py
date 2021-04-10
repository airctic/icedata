__all__ = ["parser"]

from icevision.all import *
from icevision.core.record_defaults import KeypointsRecord


def parser(data_dir: Path):
    annotations_filepath = data_dir / "biwi_sample/centers.pkl"
    img_dir = data_dir / "biwi_sample/images/"

    return BIWIParser(annotations_filepath=annotations_filepath, img_dir=img_dir)


class BIWIKeypointsMetadata(KeypointsMetadata):
    labels = ["nose"]


class BIWIParser(Parser):
    def __init__(self, annotations_filepath, img_dir, idmap=None):
        super().__init__(template_record=self.template_record(), idmap=idmap)
        self.annotations_dict = pickle.load(open(Path(annotations_filepath), "rb"))
        self.img_dir = Path(img_dir)
        self.class_map = ClassMap(["nose"])

    def __iter__(self):
        yield from self.annotations_dict.items()

    def __len__(self):
        return len(self.annotations_dict)

    def template_record(self) -> BaseRecord:
        return KeypointsRecord()

    def record_id(self, o):
        return int(o[0].replace(".jpg", ""))

    def filepath(self, o):
        return self.img_dir / o[0]

    def keypoints(self, o):
        y, x = o[1].tolist()
        return [KeyPoints.from_xyv([x, y, 1], BIWIKeypointsMetadata)]

    def image_width_height(self, o) -> Tuple[int, int]:
        return get_img_size(self.filepath(o))

    def labels(self, o) -> List[Hashable]:
        return [1]

    def bboxes(self, o) -> List[BBox]:
        w, h = get_img_size(self.filepath(o))
        return [BBox.from_xywh(0, 0, w, h)]

    def parse_fields(self, o, record, is_new):
        if is_new:
            record.set_filepath(self.filepath(o))
            record.set_img_size(self.image_width_height(o))

        record.detection.set_class_map(self.class_map)
        record.detection.add_labels_by_id(self.labels(o))
        record.detection.add_bboxes(self.bboxes(o))
        record.detection.add_keypoints(self.keypoints(o))
