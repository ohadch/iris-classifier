import os
import dotenv
dotenv.load_dotenv()

HOST = os.environ.get("HOST", '0.0.0.0')
PORT = os.environ.get("PORT", 8081)
ENV = os.environ.get("ENV", "production")

DEBUG = ENV == 'development'

ALLOWED_IMG_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOADS_DIR = "/uploads"
