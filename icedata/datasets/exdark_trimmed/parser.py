# AUTHOR: Lucas Vazquez
# Minor modifications made by Rahul Somani
#   * Removed `object_class` as a classification task
#   * Some minor changes to make compatible with icevision 0.7+
#   * Mild reorganisation

__all__ = ["parser"]

from icevision.all import *


EXDARK_CLASSIFIER_NAMES = ["lighting", "location"]
EXDARK_TEMPLATE_RECORD = BaseRecord(
    [
        FilepathRecordComponent(),
        *[
            ClassificationLabelsRecordComponent(task=tasks.Task(name=o))
            for o in EXDARK_CLASSIFIER_NAMES
        ],
        BBoxesRecordComponent(),
        InstancesLabelsRecordComponent(),
    ]
)


# TODO: Use splits specific in imageclasslist.txt
class ExDarkParser(Parser):
    # fmt: off
    LOCATION_CLASSES = [None, "Indoor", "Outdoor"]
    LIGHTING_CLASSES = [
        None, "Low", "Ambient", "Object", "Single", "Weak",
        "Strong", "Screen", "Window", "Shadow", "Twilight",
    ]
    OBJECT_CLASSES = [
        None,"Bicycle", "Boat", "Bottle", "Bus", "Car", "Cat",
        "Chair", "Cup", "Dog", "Motorbike", "People", "Table",
    ]

    # fmt: on

    def __init__(
        self,
        template_record,
        instances_annotations_dir,
        classification_annotation_filepath,
        imgs_dir,
    ):
        super().__init__(template_record=template_record)

        self.instances_annotations_dir = instances_annotations_dir
        self.classification_annotation_filepath = classification_annotation_filepath
        self.imgs_dir = imgs_dir

        self.instances_annotations_filepaths = get_files(
            instances_annotations_dir, extensions=[".txt"]
        )
        self.classification_annotation_lines = (
            classification_annotation_filepath.read_text().strip().split("\n")[1:]
        )

        self.object_class_map = ClassMap(self.OBJECT_CLASSES, background=None)
        self.lighting_class_map = ClassMap(self.LIGHTING_CLASSES, background=None)
        self.location_class_map = ClassMap(self.LOCATION_CLASSES, background=None)

        # Convenience container
        self.CLASS_MAPS = dict(
            detection=self.object_class_map,
            lighting=self.lighting_class_map,
            location=self.location_class_map,
        )

    def __iter__(self) -> Any:
        for line in self.classification_annotation_lines:
            yield line, tasks.classification

        for filepath in self.instances_annotations_filepaths:
            yield filepath, tasks.detection

    def __len__(self):
        return len(self.instances_annotations_filepaths) + len(
            self.classification_annotation_lines
        )

    def record_id(self, o) -> Hashable:
        item, task = o
        if task == tasks.detection:
            return Path(
                item.stem
            ).stem  # item is `2015_05235.jpg.txt`, stem will give `2015_05235.jpg`, stem again for `2015_05235`
        if task == tasks.classification:
            return Path(item.split()[0]).stem  # will also give `2015_05235`
        # before were using with file extension, but one can have .JPG while the other .jpg

    def parse_fields(self, o, record, is_new):
        item, task = o

        if task == tasks.detection:
            self.parse_detection(item, record)
        elif task == tasks.classification:
            self.parse_classification(item, record)
        else:
            raise ValueError

    def parse_detection(self, filepath, record):
        # the following doesn't work, filepath.stem can be `2015_00391.jpg` but actual image name is `2015_00391.JPG`
        #         img_filepath = self.imgs_dir / filepath.parent.stem / filepath.stem
        #         record.set_filepath(img_filepath)
        #         record.set_img_size(get_img_size(img_filepath))
        record.detection.set_class_map(self.object_class_map)

        lines = filepath.read_text().strip().split("\n")[1:]
        for line in lines:
            tokens = line.split()

            object_class = tokens[0]
            xywh = [int(coord) for coord in tokens[1:5]]
            bbox = BBox.from_xywh(*xywh)

            record.detection.add_labels([object_class])
            record.detection.add_bboxes([bbox])

    def parse_classification(self, line, record):
        tokens = line.split()
        img_name = tokens[0]
        object_class, lighting, location, _ = [int(id) for id in tokens[1:]]

        # common
        object_class_name = self.object_class_map.get_by_id(object_class)
        filepath = self.imgs_dir / object_class_name / img_name
        record.set_filepath(filepath)
        record.set_img_size(get_img_size(filepath))

        # classification
        # record.object_class.set_class_map(self.object_class_map)
        # record.object_class.add_labels_by_id([object_class])

        record.lighting.set_class_map(self.lighting_class_map)
        record.lighting.add_labels_by_id([lighting])

        record.location.set_class_map(self.location_class_map)
        record.location.add_labels_by_id([location])


def parser(data_dir: Path):
    parser = ExDarkParser(
        template_record=EXDARK_TEMPLATE_RECORD,
        instances_annotations_dir=data_dir / "annotations",
        classification_annotation_filepath=data_dir / "imageclasslist.txt",
        imgs_dir=data_dir / "images",
    )

    return parser
