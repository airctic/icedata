import icedata
from icevision.all import *


def test_fridge_class_map():
    num_classes = icedata.fridge.NUM_CLASSES
    class_map = icedata.fridge.class_map()

    assert num_classes == len(class_map) == 5
    assert class_map.get_id(0) == "background"
    assert class_map.get_id(-1) == "water_bottle"


def test_fridge_parser(data_dir):
    class_map = icedata.fridge.class_map()
    parser = icedata.fridge.parser(data_dir, class_map=class_map)

    records = parser.parse()[0]
    assert len(records) == 5
    record = records[0]

    expected = {"imageid", "labels", "bboxes", "filepath", "height", "width"}
    assert set(record.keys()) == expected

    assert record["filepath"].name == "10.jpg"
    assert record["imageid"] == 0
    assert record["labels"] == [2, 3]
    assert record["height"] == 666
    assert record["width"] == 499

    expected = [BBox.from_xyxy(86, 102, 216, 439), BBox.from_xyxy(150, 377, 445, 490)]
    assert record["bboxes"] == expected