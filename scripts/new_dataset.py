import fire
import icedata


def new_dataset(dataset_name: str):
    """Generates the basic skeleton for a new dataset.

    # Arguments
        dataset_name: The name of the dataset, must be unique.
    """
    icedata.template.generate_dataset(dataset_name)


if __name__ == "__main__":
    fire.Fire(new_dataset)
