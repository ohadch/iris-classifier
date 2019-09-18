import os
import dotenv
dotenv.load_dotenv()

HOST = os.environ.get("HOST", '0.0.0.0')
PORT = os.environ.get("PORT", 8000)
ENV = os.environ.get("ENV", "production")

DEBUG = ENV == 'development'

ALLOWED_IMG_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
MODELS_FOLDER = os.path.join(os.getcwd(), "trained_models")
