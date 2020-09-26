__all__ = ["NUM_CLASSES", "class_map", "load_data", "load"]

from icevision.imports import *
from icevision.core import *
from icevision.utils import *


# IMPLEMENT: Number of classes plus 1 for background
NUM_CLASSES = 0 + 1

def class_map(background: int = 0) -> ClassMap:
    """Creates the `ClassMap` specific for this dataset.

    # Arguments
        background: Label id to use for background.

    # Returns
        A `ClassMap`.
    """
    raise NotImplementedError


def load_data(force_download: bool = False):
    """Loads the data from disk or download from the internet if necessary.
    """
    raise NotImplementedError
