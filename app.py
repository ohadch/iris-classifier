import os

from flask import Flask, jsonify, request, render_template
from sklearn import svm
from sklearn import datasets
from sklearn.externals import joblib

from settings import HOST, PORT, DEBUG

# initialize flask application
app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


@app.route('/api/train', methods=['POST'])
def train():
    # get parameters from request
    parameters = request.get_json()

    # read iris data set
    iris = datasets.load_iris()
    X, y = iris.data, iris.target

    # fit model
    clf = svm.SVC(C=float(parameters['C']),
                  probability=True,
                  random_state=1)

    clf.fit(X, y)

    # persist model
    joblib.dump(clf, 'model.pkl')
    return jsonify({'accuracy': round(clf.score(X, y) * 100, 2)})


if __name__ == '__main__':
    # run web server
    app.run(host=HOST, debug=DEBUG, port=PORT)