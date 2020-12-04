__all__ = ["load_data"]

from icevision.imports import *


def load_data():
    return logger.info(
        """
    MANUALLY download AND unzip the dataset from https://cg.cs.tsinghua.edu.cn/dataset/form.html?dataset=ochuman. 
    You will need the path to the `ochuman.json` annotations file and the `images` directory.
    """
    )
