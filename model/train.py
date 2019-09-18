import sys
from utils.model import train

DATASET_NAME = sys.argv[1]

if __name__ == '__main__':
    train(DATASET_NAME)
