__all__ = ["generate_dataset"]

from icevision.imports import *
from icevision.utils import *


def generate_dataset(dataset_name: str):
    this_path = Path(__file__).absolute()
    templates_dir = this_path.parent.parent.parent / "templates/dataset"
    datasets_dir = this_path.parent.parent / "datasets"

    new_dataset_dir = datasets_dir / dataset_name
    try:
        new_dataset_dir.mkdir()
    except FileExistsError:
        raise FileExistsError(
            f"A dataset named {dataset_name} already exists, try a different name"
        )

    template_files = get_files(templates_dir, extensions=[".py", ".md"])
    for template_file in template_files:
        text = template_file.read_text()

        # do stuff with the file
        text = re.sub(r"TK_DATASET_NAME", dataset_name, text)

        new_filepath = (
            datasets_dir / dataset_name / template_file.relative_to(templates_dir)
        )
        new_filepath.parent.mkdir(exist_ok=True)
        with open(str(new_filepath), "w") as new_file:
            new_file.write(text)

    # append to init
    import_statement = f"from icedata.datasets import {dataset_name}\n"
    init_filepath = datasets_dir / "__init__.py"
    init_lines = init_filepath.readlines()
    init_lines.append(import_statement)

    with open(init_filepath, "w") as init_file:
        init_file.write("".join(init_lines))
