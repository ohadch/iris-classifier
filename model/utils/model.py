import os
import subprocess
import sys

from settings import DATASETS_FOLDER, TRAINING_STEPS


def train(dataset_name: str) -> dict:
    """
    Trains the model based on the input dataset
    :param dataset_name: The path to the dataset train data
    :return: The image classification
    """
    dataset_folder = os.path.join(DATASETS_FOLDER, dataset_name)

    if not os.path.exists(dataset_folder):
        raise ValueError(f"Dataset does not exist: {dataset_name}")

    # python3
    # retrain.py --bottleneck_dir = bottlenecks --how_many_training_steps
    # 500 --model_dir = inception --output_graph = retrained_graph.pb --output_labels = retrained_labels.txt --image_dir
    # flower_photos /

    retrained_graph_path = os.path.abspath(os.path.join("..", "trained_models", f"{dataset_name}_graph.pb"))
    retrained_labels_path = os.path.abspath(os.path.join("..", "trained_models", f"{dataset_name}_labels.txt"))

    print(f"Training {dataset_name}, folder = {dataset_folder}")
    p = subprocess.Popen([
        sys.executable,
        "retrain.py",
        "--bottleneck_dir=bottlenecks",
        "--how_many_training_steps",
        str(TRAINING_STEPS),
        "--model_dir=inception",
        f"--output_graph={retrained_graph_path}",
        f"--output_labels={retrained_labels_path}",
        f"--image_dir={dataset_folder}"

    ], stdout=subprocess.PIPE, shell=False)
    out, err = p.communicate()

    # result = out.split('\n')
    if err is not None:
        raise RuntimeError(err)

