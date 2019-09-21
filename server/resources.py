import os

from werkzeug.utils import secure_filename
from utils.upload import allowed_file
from flask import request, jsonify
from flask_restful import Resource, reqparse
from _sqlalchemy import UserModel, RevokedTokenModel
from flask_jwt_extended import create_access_token, create_refresh_token, \
    jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt
from utils.classifier import classify
from settings import UPLOAD_FOLDER

parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required = True)
parser.add_argument('password', help='This field cannot be blank', required = True)


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'error': 'User {} already exists'.format(data['username'])}

        new_user = UserModel(
            username=data['username'],
            password=UserModel.generate_hash(data['password'])
        )

        try:
            new_user.save_to_db()
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])
            return {
                'message': 'User {} was created'.format(data['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = UserModel.find_by_username(data['username'])

        if not current_user:
            return {'error': 'User {} doesn\'t exist'.format(data['username'])}

        if UserModel.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])
            return {
                'username': data['username'],
                'message': 'Logged in as {}'.format(current_user.username),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        else:
            return {'error': 'Wrong credentials'}


class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}


class AllUsers(Resource):
    def get(self):
        return UserModel.return_all()

    def delete(self):
        return UserModel.delete_all()


class SecretResource(Resource):
    @jwt_required
    def get(self):
        return {
            'answer': 42
        }


class ImageClassification(Resource):
    @jwt_required
    def post(self):
        # check if the post request has the file part
        if request.files.get('file') is None:
            return jsonify({'error': 'no file has been provided'})

        file = request.files['file']

        # Process file if it is allowed
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            full_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(full_path)

            # Classifies the image
            classification = classify(full_path, 'flower_photos')

            # Removes the uploaded image
            os.remove(full_path)

            return jsonify({'classification': classification})
