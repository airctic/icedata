import icedata


def test_class_map():
    num_classes = icedata.coco.NUM_CLASSES
    class_map = icedata.coco.class_map()

    assert num_classes == len(class_map) == 91
    assert class_map.get_id(0) == "background"
    assert class_map.get_id(-1) == "toothbrush"
