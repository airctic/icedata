import icedata
from icevision.all import *


def test_parser(data_dir):
    class_map = icedata.pets.class_map()
    parser = icedata.pets.parser(data_dir, class_map=class_map, mask=True)

    records = parser.parse(data_splitter=SingleSplitSplitter())[0]
    assert len(records) == 5
    record = records[0]

    expected = {"imageid", "labels", "bboxes", "filepath", "height", "width", "masks"}
    assert set(record.keys()) == expected

    assert record["filepath"].name == "Abyssinian_119.jpg"
    assert record["imageid"] == 0
    assert record["labels"] == [1]
    assert record["height"] == 297
    assert record["width"] == 300

    assert record["bboxes"] == [BBox.from_xyxy(39, 51, 156, 179)]
    assert record["masks"][0].filepath.name == "Abyssinian_119.png"
