import icedata
from icevision.all import *


def test_parser(data_dir):
    parser = icedata.ochuman.parser(
        data_dir / "annotations/ochuman.json", data_dir / "images"
    )

    records = parser.parse(data_splitter=SingleSplitSplitter())[0]
    assert len(records) == 10
    record = records[3]

    assert record.filepath.name == "000004.jpg"
    assert record.record_id == 3
    assert record.detection.labels == ["person", "person"]
    assert record.height == 333
    assert record.width == 500
