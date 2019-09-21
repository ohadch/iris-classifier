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


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
