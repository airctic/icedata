__all__ = ["parser"]

from icevision.all import *
from icevision.core.record_defaults import KeypointsRecord


def parser(annotations_path: Union[str, Path], img_dir_path: Union[str, Path]):
    return OCHumanParser(
        annotations_filepath=Path(annotations_path), img_dir=Path(img_dir_path)
    )


class OCHConnectionsColor:
    head = (220, 30, 200)
    torso = (100, 240, 100)
    right_arm = (170, 170, 100)
    left_arm = (120, 120, 230)
    left_leg = (230, 120, 130)
    right_leg = (230, 180, 190)


class OCHKeypointsMetadata(KeypointsMetadata):
    labels = (
        "right_shoulder",
        "right_elbow",
        "right_wrist",
        "left_shoulder",
        "left_elbow",
        "left_wrist",
        "right_hip",
        "right_knee",
        "right_ankle",
        "left_hip",
        "left_knee",
        "left_ankle",
        "head",
        "neck",
        "right_ear",
        "left_ear",
        "nose",
        "right_eye",
        "left_eye",
    )

    # connections = (
    #     KeypointConnection(15, 18, OCHConnectionsColor.head),
    #     KeypointConnection(12, 16, OCHConnectionsColor.head),
    #     KeypointConnection(3, 4, OCHConnectionsColor.left_arm),
    #     KeypointConnection(18, 16, OCHConnectionsColor.head),
    #     KeypointConnection(16, 13, OCHConnectionsColor.head),
    #     KeypointConnection(4, 5, OCHConnectionsColor.left_arm),
    #     KeypointConnection(16, 17, OCHConnectionsColor.head),
    #     KeypointConnection(13, 3, OCHConnectionsColor.torso),
    #     KeypointConnection(0, 1, OCHConnectionsColor.right_arm),
    #     KeypointConnection(17, 14, OCHConnectionsColor.head),
    #     KeypointConnection(13, 0, OCHConnectionsColor.torso),
    #     KeypointConnection(1, 2, OCHConnectionsColor.right_arm),
    #     KeypointConnection(3, 9, OCHConnectionsColor.torso),
    #     KeypointConnection(0, 6, OCHConnectionsColor.torso),
    #     KeypointConnection(9, 6, OCHConnectionsColor.torso),
    #     KeypointConnection(9, 10, OCHConnectionsColor.left_leg),
    #     KeypointConnection(6, 7, OCHConnectionsColor.right_leg),
    #     KeypointConnection(10, 11, OCHConnectionsColor.left_leg),
    #     KeypointConnection(7, 8, OCHConnectionsColor.right_leg),
    #     KeypointConnection(15, 3, OCHConnectionsColor.head),
    #     KeypointConnection(14, 0, OCHConnectionsColor.head),
    # )


class OCHumanParser(Parser):
    def __init__(self, annotations_filepath, img_dir):
        super().__init__(template_record=self.template_record())
        self.annotations_dict = json.loads(Path(annotations_filepath).read_bytes())
        self.img_dir = Path(img_dir)
        self.class_map = ClassMap(["person"])

    def __iter__(self):
        yield from self.annotations_dict["images"]

    def __len__(self):
        return len(self.annotations_dict["images"])

    def template_record(self):
        return KeypointsRecord()

    def record_id(self, o):
        return int(o["image_id"])

    def parse_fields(self, o, record: BaseRecord, is_new: bool) -> None:
        if is_new:
            record.set_filepath(self.filepath(o))
            record.set_img_size(self.image_width_height(o))
            record.detection.set_class_map(self.class_map)

        record.detection.add_labels(self.labels(o))
        record.detection.add_bboxes(self.bboxes(o))
        record.detection.add_keypoints(self.keypoints(o))

    def filepath(self, o):
        return self.img_dir / o["file_name"]

    def keypoints(self, o):
        return [
            KeyPoints.from_xyv(kps["keypoints"], OCHKeypointsMetadata)
            for kps in o["annotations"]
            if kps["keypoints"] is not None
        ]

    def image_width_height(self, o) -> Tuple[int, int]:
        return get_img_size(self.filepath(o))

    def labels(self, o) -> List[Hashable]:
        return ["person" for ann in o["annotations"] if ann["keypoints"] is not None]

    def bboxes(self, o) -> List[BBox]:
        return [
            BBox.from_xyxy(*ann["bbox"])
            for ann in o["annotations"]
            if ann["keypoints"] is not None
        ]
