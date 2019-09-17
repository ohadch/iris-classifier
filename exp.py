import os
import sys

from utils.classifier import classify
from settings import UPLOAD_FOLDER

IMAGE_PATH = os.path.join(UPLOAD_FOLDER, sys.argv[1])

classification = classify(IMAGE_PATH)
print(classification)