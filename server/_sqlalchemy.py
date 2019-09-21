from passlib.hash import pbkdf2_sha256 as sha256

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from settings import UPLOAD_FOLDER, VERSION, POSTGRES_URI
from logger import logger

# initialize flask application
app = Flask(__name__,
            static_folder="./react/build/static",
            template_folder="./react/build")

app.config["SQLALCHEMY_DATABASE_URI"] = POSTGRES_URI
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

logger.info(f"App version: {VERSION}")


db = SQLAlchemy(app)
jwt = JWTManager(app)


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'username': x.username,
                'password': x.password
            }

        return {'users': list(map(lambda x: to_json(x), UserModel.query.all()))}

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
        except:
            return {'message': 'Something went wrong'}

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    server_path = db.Column(db.String(255), unique=True, nullable=False)
    classification = db.Column(db.String(50), nullable=True)
    classification_success = db.Column(db.Boolean, nullable=True)


class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)