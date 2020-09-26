__all__ = ["generate_dataset"]

from icevision.imports import *
from icevision.utils import *


def generate_dataset(dataset_name: str):
    this_path = Path(__file__).absolute()
    templates_dir = this_path.parent.parent.parent / "templates/dataset"
    datasets_dir = this_path.parent.parent / "datasets"

    new_dataset_dir = datasets_dir / dataset_name
    new_dataset_dir.mkdir(exist_ok=True)

    template_files = get_files(templates_dir, extensions=[".py"])
    for template_file in template_files:
        text = template_file.read()
        # do stuff with the file

        new_filepath = datasets_dir / dataset_name / template_file.name
        with open(str(new_filepath), "w") as new_file:
            new_file.write(text)
