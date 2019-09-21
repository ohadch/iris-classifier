import os
import resources

from flask import jsonify, request, render_template
from flask_restful import Api

from werkzeug.utils import secure_filename

from _sqlalchemy import app, db
from settings import HOST, PORT, DEBUG
from utils.upload import allowed_file
from utils.classifier import classify

api = Api(app)


@app.before_first_request
def create_tables():
    # Creates all SQLAlchemy model tables
    db.create_all()


@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)


@app.route('/')
def react():
    return render_template("index.html")


@app.route('/api')
def api_home():
    return jsonify({'message': 'This is Iris Classifier'})


@app.route("/api/file", methods=['POST'])
def upload_file():
    if request.method == 'POST':

        # check if the post request has the file part
        if request.files.get('file') is None:
            return jsonify({'error': 'no file has been provided'})

        file = request.files['file']

        # Process file if it is allowed
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            full_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(full_path)

            # Classifies the image
            classification = classify(full_path, 'flower_photos')

            # Removes the uploaded image
            os.remove(full_path)

            return jsonify({'classification': classification})


api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.SecretResource, '/secret')

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
