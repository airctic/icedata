import icedata


def test_class_map():
    num_classes = icedata.pets.NUM_CLASSES
    class_map = icedata.pets.class_map()

    assert num_classes == len(class_map) == 38
    assert class_map.get_id(0) == "background"
    assert class_map.get_id(-1) == "yorkshire_terrier"
