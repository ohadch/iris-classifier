import os
import re
import subprocess
import sys

from pprint import pprint
from settings import MODELS_FOLDER


def classify(image_path: str, dataset_name) -> dict:
    """
    Classifies a flower image to its type.
    :param image_path: The path to the flower image.
    :param dataset_name: The dataset name for the image to be classified
    :return: The image classification
    """
    model_path = os.path.join(MODELS_FOLDER, f"{dataset_name}_graph.pb")

    # Validate model exists
    if not os.path.exists(model_path):
        raise ValueError(f"Model does not exist: {model_path}")

    # Classify the image
    print(f"Classifying: {image_path}, model path: {model_path}")
    p = subprocess.Popen([
        sys.executable,
        "label_image.py",
        "--graph=retrained_graph.pb",
        f'--image={image_path}',
        "--labels=retrained_labels.txt",
        "--output_layer=final_result",
        "--input_layer=Placeholder"
    ], stdout=subprocess.PIPE, shell=False)
    out, err = p.communicate()

    # result = out.split('\n')
    if err is not None:
        raise RuntimeError(err)

    output = out.decode()
    print(f"OUTPUT: {output}")


    # Classify the image
    classification = dict([re.compile(r"\s+").split(foo) for foo in .strip().split("\n")])
    pprint(classification)

    return classification
