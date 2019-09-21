import os
import dotenv

ENV = os.environ.get("ENV", "production")

# Load from dotenv only in development
if ENV == 'development':
    dotenv.load_dotenv()

HOST = os.environ.get("HOST", '0.0.0.0')
PORT = os.environ.get("PORT", 8000)

DEBUG = ENV == 'development'

ALLOWED_IMG_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
MODELS_FOLDER = os.path.join(os.getcwd(), "trained_models")

VERSION = '1.0.1'
