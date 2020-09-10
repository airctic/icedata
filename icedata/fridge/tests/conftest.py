import pytest
from icevision.imports import *


@pytest.fixture()
def data_dir():
    return Path(__file__).absolute().parent.parent / "sample_data"
