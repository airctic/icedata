from icevision.imports import *
from icevision.utils import *
import icedata


def test_generate_dataset():
    dataset_name = "test_ds"
    datasets_dir = Path(icedata.datasets.__file__).absolute().parent
    new_dataset_path = datasets_dir / dataset_name
    init_filepath = datasets_dir / "__init__.py"
    original_init_lines = init_filepath.readlines()

    if new_dataset_path.exists():
        shutil.rmtree(new_dataset_path)

    icedata.template.generate_dataset(dataset_name)

    # check files
    assert new_dataset_path.exists()
    filenames = [str(o.relative_to(datasets_dir)) for o in get_files(new_dataset_path)]
    assert set(filenames) == {
        "test_ds/__init__.py",
        "test_ds/data.py",
        "test_ds/parser.py",
        "test_ds/trained_models.py",
        "test_ds/README.md",
        "test_ds/tests/__init__.py",
        "test_ds/tests/test_data.py",
        "test_ds/tests/test_trained_models.py",
        "test_ds/tests/test_parser.py",
        "test_ds/tests/conftest.py",
        "test_ds/sample_data/README.md",
    }

    # check init
    init_lines = init_filepath.readlines()
    expected_import = f"from icedata.datasets import {dataset_name}\n"
    assert init_lines[-1] == expected_import

    # revert changes
    shutil.rmtree(new_dataset_path)
    with open(init_filepath, "w") as init_file:
        init_file.write("".join(original_init_lines))
