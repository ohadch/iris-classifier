import os

from flask import Flask, jsonify, request, render_template
from werkzeug.utils import secure_filename

from settings import HOST, PORT, UPLOAD_FOLDER, VERSION, DEBUG
from utils.upload import allowed_file
from utils.classifier import classify

from logger import logger

# initialize flask application
app = Flask(__name__,
            static_folder="./react/build/static",
            template_folder="./react/build")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

logger.info(f"App version: {VERSION}")


@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)


@app.route('/')
def react():
    return render_template("index.html")


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


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
