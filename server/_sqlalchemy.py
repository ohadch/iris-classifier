from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from settings import UPLOAD_FOLDER, VERSION, DB_TYPE, \
    POSTGRES_HOST, POSTGRES_PORT, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB
from logger import logger

# initialize flask application
app = Flask(__name__,
            static_folder="./react/build/static",
            template_folder="./react/build")
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

logger.info(f"App version: {VERSION}")

DB_URI = '{db_type}://{user}:{password}@{host}:{port}/{db_name}'.format(
    db_type=DB_TYPE,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=POSTGRES_PORT,
    db_name=POSTGRES_DB,
)

db = SQLAlchemy(app)
