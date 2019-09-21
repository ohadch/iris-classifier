from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from settings import UPLOAD_FOLDER, VERSION, POSTGRES_URI
from logger import logger

# initialize flask application
app = Flask(__name__,
            static_folder="./react/build/static",
            template_folder="./react/build")
app.config["SQLALCHEMY_DATABASE_URI"] = POSTGRES_URI
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

logger.info(f"App version: {VERSION}")


db = SQLAlchemy(app)
