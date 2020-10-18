import icedata
from icevision.all import *


def test_parser(data_dir):
    class_map = icedata.coco.class_map()
    parser = icedata.coco.parser(
        annotations_file=data_dir / "annotations.json", img_dir=data_dir / "images"
    )

    records = parser.parse(data_splitter=SingleSplitSplitter())[0]
    assert len(records) == 5
    r = records[2]

    assert (r["height"], r["width"]) == (427, 640)
    assert r["imageid"] == 2
    assert r["bboxes"][0].xywh == (0.0, 73.89, 416.44, 305.13)
    assert r["filepath"] == data_dir / "images/000000128372.jpg"
