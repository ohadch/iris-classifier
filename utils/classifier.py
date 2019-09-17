import os
import subprocess
import sys


def classify(image_path: str) -> dict:
    """
    Classifies a flower image to its type.
    :param image_path: The path to the flower image.
    :return: The image classification
    """
    print(f"Classifying: {image_path}")
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

    classification = out.decode().strip().split("\n")
    return classification
