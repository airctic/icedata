import icedata


def test_class_map():
    num_classes = icedata.pennfudan.NUM_CLASSES
    class_map = icedata.pennfudan.class_map()

    assert num_classes == len(class_map) == 2
    assert class_map.get_id(0) == "background"
    assert class_map.get_id(-1) == "person"
