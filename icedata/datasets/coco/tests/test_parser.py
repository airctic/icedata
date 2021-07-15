import icedata
from icevision.all import *


def test_parser(data_dir):
    class_map = icedata.coco.class_map()
    parser = icedata.coco.parser(
        annotations_file=data_dir / "annotations.json", img_dir=data_dir / "images"
    )

    records = parser.parse(data_splitter=SingleSplitSplitter())[0]
    assert len(records) == 5
    record = records[2]

    assert (record.height, record.width) == (427, 640)
    assert record.record_id == 2
    assert record.detection.bboxes[0].xywh == (0.0, 73.89, 416.44, 305.13)
    assert record.filepath == data_dir / "images/000000128372.jpg"
