import icedata
from icevision.all import *


def test_parser(data_dir):
    parser = icedata.pets.parser(data_dir, class_map=None, mask=True)

    records = parser.parse(data_splitter=SingleSplitSplitter())[0]
    assert len(records) == 5
    record = records[0]

    expected = {
        "bboxes",
        "class_map",
        "filepath",
        "height",
        "imageid",
        "labels",
        "masks",
        "width",
    }
    assert set(record.keys()) == expected

    assert record["filepath"].name == "Abyssinian_119.jpg"
    assert record["imageid"] == 0
    assert record["labels"] == [1]
    assert record["height"] == 297
    assert record["width"] == 300

    assert record["bboxes"] == [BBox.from_xyxy(39, 51, 156, 179)]
    assert record["masks"] == EncodedRLEs(
        [
            {
                "size": [297, 300],
                "counts": b"fQ9:l86L3L5aHAk5f0nI@T1;n19jL_OS1>o1c1jMdNR2^1jMfNT2\\1dMmNY2V1bMoN\\2R1aMRO]2o0aMSO]2o0aMTO]2n0_MUO`2l0^MVO`2m0]MUOb2o0XMTOg2P1TMROk2g300O1O100O10000O2N2O1O3M:Fe0[O2NO1O1O1O1O1O1O2N1O1O2N1O1O1O2N1O2N1O00000000000000000000000000000000000000000000000000000000000000000000O100O100O1O1O1O100O1O1O1O1O1O1O100O1O1O1O1O1O1O100O1O100O10000O1000oJbNW2]1^MoNb2Q1oL_OP3b0jLCV3=gLFY3:fLHY39dLJ[37aLL_35^LNa34ZLOf34PL4o3OjK5V4`2O1O1O001O1O1O001O00001O1O001O1O1O1O001O1O001O1O001O001O00001O1O00001O1O001O1O001O001O00001O1O1O1O2N2N3M2N3M2N3M4L>B8H3M4L3M4L1OO1O1O1O1O1O1M3O00000O1O10000001N1N200O2O0N201N1N2O2O1N10000N2O1O2N100N3N2M2N3N2O1O1O1N2O2N1O1N3N1N3N2M3L6IfU6",
            }
        ]
    )
