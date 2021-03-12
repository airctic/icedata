import icedata
from icevision.all import *


def test_parser(data_dir):
    parser = icedata.pennfudan.parser(data_dir)

    records = parser.parse(data_splitter=SingleSplitSplitter())[0]
    assert len(records) == 5
    record = records[0]

    expected = {
        "bboxes",
        "class_map",
        "filepath",
        "height",
        "imageid",
        "iscrowds",
        "labels",
        "masks",
        "width",
    }

    assert set(record.keys()) == expected

    assert record["filepath"].name == "FudanPed00001.png"
    assert record["imageid"] == 0
    assert record["labels"] == [1, 1]
    assert record["height"] == 536
    assert record["width"] == 559

    expected = [BBox.from_xyxy(160, 182, 302, 431), BBox.from_xyxy(420, 171, 535, 486)]
    assert record["bboxes"] == expected
