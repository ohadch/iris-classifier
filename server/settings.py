import os
import dotenv

# Load from dotenv only in development
if 'DOCKER' not in os.environ:
    dotenv.load_dotenv()

ENV = os.environ.get("ENV", "production")

# App host
HOST = os.environ.get("HOST", '0.0.0.0')
PORT = os.environ.get("PORT", 8000)
VERSION = '1.0.1'

# Postgres
POSTGRES_HOST = os.environ['POSTGRES_HOST']
POSTGRES_PORT = os.environ['POSTGRES_PORT']
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']

# Debug mode
DEBUG = ENV == 'development'

# Classification config
ALLOWED_IMG_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
MODELS_FOLDER = os.path.join(os.getcwd(), "trained_models")
