import os
import dotenv

# Load from dotenv only in development
if 'DOCKER' not in os.environ:
    dotenv.load_dotenv()

ENV = os.environ.get("ENV", "production")

HOST = os.environ.get("HOST", '0.0.0.0')
PORT = os.environ.get("PORT", 8000)

DEBUG = ENV == 'development'

ALLOWED_IMG_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
MODELS_FOLDER = os.path.join(os.getcwd(), "trained_models")

VERSION = '1.0.1'
