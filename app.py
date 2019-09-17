import os

from flask import Flask, jsonify, request, render_template
from werkzeug.utils import secure_filename

from settings import HOST, PORT, DEBUG
from utils.upload import allowed_file

# initialize flask application
app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


@app.route("/file", methods=['POST'])
def upload_file():
    if request.method == 'POST':

        # check if the post request has the file part
        if 'file' not in request.files:
            return jsonify({'error': 'no file has been provided'})

        file = request.files['file']

        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return jsonify({'error': 'file must have a name'})

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify({'message': 'file has been uploaded successfully'})


if __name__ == '__main__':
    # run web server
    app.run(host=HOST, debug=DEBUG, port=PORT)