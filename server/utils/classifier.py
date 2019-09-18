import os
import re
import subprocess
import sys

from pprint import pformat
from settings import MODELS_FOLDER

from logger import logger


def classify(image_path: str, dataset_name) -> dict:
    """
    Classifies a flower image to its type.
    :param image_path: The path to the flower image.
    :param dataset_name: The dataset name for the image to be classified
    :return: The image classification
    """
    graph_path = os.path.join(MODELS_FOLDER, f"{dataset_name}_graph.pb")
    labels_path = os.path.join(MODELS_FOLDER, f"{dataset_name}_labels.txt")

    # Validate model exists
    if not os.path.exists(graph_path):
        raise ValueError(f"Graph does not exist: {graph_path}")

    if not os.path.exists(labels_path):
        raise ValueError(f"Labels do not exist: {labels_path}")

    # Classify the image
    logger.info(f"Classifying: {image_path}, model path: {graph_path}")
    p = subprocess.Popen([
        sys.executable,
        "label_image.py",
        f"--graph={graph_path}",
        f'--image={image_path}',
        f"--labels={labels_path}",
        "--output_layer=final_result",
        "--input_layer=Placeholder"
    ], stdout=subprocess.PIPE, shell=False)
    out, err = p.communicate()

    if err is not None:
        raise RuntimeError(err)

    # Decode the output
    output = out.decode()
    logger.info(f"OUTPUT: {output}")

    # Check empty classification
    if output == '' or output is None:
        logger.error(err)
        raise ValueError("Classification was not produced")

    # Parse the result
    classification = dict([re.compile(r"\s+").split(foo) for foo in output.strip().split("\n")])
    logger.info(pformat(classification))

    return classification
