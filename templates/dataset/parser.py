__all__ = ["parser"]

from icevision.all import *

# from icevision.imports import *
# from icevision.core import *
# from icevision import parsers


def parser(data_dir: Path) -> parsers.ParserInterface:
    """Creates the Parser specific for this dataset.

    # Arguments
        data_dir: Full path to the directory the data is located

    # Returns
        The parser for this dataset.
    """
    raise NotImplementedError
