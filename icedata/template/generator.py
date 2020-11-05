__all__ = ["generate_dataset"]

from icevision.imports import *
from icevision.utils import *


def generate_dataset(dataset_name: str):
    this_path = Path(__file__).absolute()
    templates_dir = this_path.parent.parent.parent / "templates/dataset"
    datasets_dir = this_path.parent.parent / "datasets"

    new_dataset_dir = datasets_dir / dataset_name
    try:
        print(f"\n- Trying to create {new_dataset_dir} folder\n")
        new_dataset_dir.mkdir()
        print(f"- {new_dataset_dir} folder created\n")
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
            print(f"   - {new_filepath.relative_to(datasets_dir)} file created\n")

    # append to init
    icedata_dir = Path(__file__).resolve().parents[1]
    print("icedata_dir: ", icedata_dir)

    # Get the existing datasets list
    dir_to_search = icedata_dir / "datasets"
    ds_dirlist = sorted(
        [
            filename
            for filename in os.listdir(dir_to_search)
            if (
                os.path.isdir(os.path.join(dir_to_search, filename))
                and not filename.startswith("_")
            )
        ]
    )

    init_lines = []
    # Add existing datasets to list
    for ds_name in ds_dirlist:
        import_statement = f"from icedata.datasets import {ds_name}\n"
        init_lines.append(import_statement)

    # # Add new dataset to list
    # import_statement = f"from icedata.datasets import {dataset_name}\n"
    # init_lines.append(import_statement)

    # Update "__init__.py" file
    init_filepath = datasets_dir / "__init__.py"
    # init_lines = init_filepath.readlines()
    # init_lines.append(import_statement)

    with open(init_filepath, "w") as init_file:
        init_file.write("".join(init_lines))
