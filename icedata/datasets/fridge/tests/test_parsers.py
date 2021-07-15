import icedata
from icevision.all import *


def test_parser(data_dir):
    class_map = icedata.fridge.class_map()
    parser = icedata.fridge.parser(data_dir)

    records = parser.parse(data_splitter=SingleSplitSplitter())[0]
    assert len(records) == 5
    record = records[0]

    assert record.filepath.name == "10.jpg"
    assert record.record_id == 0
    assert record.height == 666
    assert record.width == 499
    assert record.detection.labels == ["carton", "milk_bottle"]

    expected = [BBox.from_xyxy(86, 102, 216, 439), BBox.from_xyxy(150, 377, 445, 490)]
    assert record.detection.bboxes == expected
