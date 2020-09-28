from icevision.imports import Path
import icedata


def test_load_data(tmpdir):
    url = "https://github.com/airctic/icedata/archive/0.0.2post1.tar.gz"

    data_dir = icedata.load_data(url, "test_data")

    assert data_dir.exists()
    assert (data_dir / "0.0.2post1.tar.gz").exists()
