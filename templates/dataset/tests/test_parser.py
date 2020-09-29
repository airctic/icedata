import icedata
from icevision.all import *


def test_parser(data_dir):
    class_map = icedata.TK_DATASET_NAME.class_map()
    parser = icedata.TK_DATASET_NAME.parser(data_dir)

    raise NotImplementedError
