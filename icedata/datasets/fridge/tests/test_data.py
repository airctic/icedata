import icedata


def test_class_map():
    num_classes = icedata.fridge.NUM_CLASSES
    class_map = icedata.fridge.class_map()

    assert num_classes == len(class_map) == 5
    assert class_map.get_id(0) == "background"
    assert class_map.get_id(-1) == "water_bottle"
