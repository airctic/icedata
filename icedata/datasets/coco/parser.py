__all__ = ["parser_bbox", "parser_mask", "parser_keypoints"]

from icevision.imports import *
from icevision.core import *
from icevision import parsers


parser_bbox = parsers.COCOBBoxParser
parser_mask = parsers.COCOMaskParser
parser_keypoints = parsers.COCOKeyPointsParser
