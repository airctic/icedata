from icevision.imports import *
from icevision.utils import *
import icedata


def test_generate_dataset():
    dataset_name = "test_ds"
    datasets_dir = Path(icedata.datasets.__file__).absolute().parent
    new_dataset_path = datasets_dir / dataset_name

    if new_dataset_path.exists():
        shutil.rmtree(new_dataset_path)

    icedata.template.generate_dataset(dataset_name)

    assert new_dataset_path.exists()
    filenames = [o.name for o in get_files(new_dataset_path)]
    assert set(filenames) == {"data.py", "parser.py", "trained_models.py"}

    shutil.rmtree(new_dataset_path)
