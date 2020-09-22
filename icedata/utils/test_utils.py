import icedata


def test_load_data():
    url = "https://github.com/airctic/icedata/archive/0.0.2post1.tar.gz"
    data_dir = icedata.load_data(url, "test_data", force_download=True)

    assert data_dir.exists()
