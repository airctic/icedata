import icedata
from icevision.all import *


def test_parser(data_dir):
    parser = icedata.biwi.parser(data_dir)

    records = parser.parse(data_splitter=SingleSplitSplitter())[0]
    assert len(records) == 6
    record = records[3]

    assert record.filepath.name == "3.jpg"
    assert record.record_id == 3
    assert record.detection.labels == ["nose"]
    assert record.height == 120
    assert record.width == 160

    expected = [BBox.from_xywh(0, 0, record.width, record.height)]
    assert record.detection.bboxes == expected

    expected = KeyPoints.from_xyv([78, 63, 1], ["nose"])
    assert [
        (int(round(x)), int(round(y)), 1)
        for x, y, v in record.detection.keypoints[0].xyv
    ] == expected.xyv
