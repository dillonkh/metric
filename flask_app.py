# from app import app

import flask
from flask import Flask, request

# from app import app
app = Flask(__name__)


import json
import os

from flask_sqlalchemy import SQLAlchemy


SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="dillonkh",
    password="HondieLand96",
    hostname="dillonkh.mysql.pythonanywhere-services.com",
    databasename="dillonkh$dummydata",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


from Service.DatasetServices import DatasetServices
from Service.ApproachServices import ApproachServices
from Service.ResultServices import ResultServices


@app.route('/')
@app.route('/index')
def index():
    signedIn = True
    if (signedIn == True):
        return flask.render_template('index.html')

    else:
        return flask.render_template('index.html')


@app.route('/signin')
def signin():
    return flask.render_template('signin.html')

@app.route('/createAccount')
def createAccount():
    return flask.render_template('create_account.html')

@app.route('/upload')
def upload():
    return flask.render_template('upload.html')

@app.route('/metrics')
def metrics():
    return flask.render_template('metrics.html')


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        f = request.files.get('file')
        filename = "{}.json".format(f.__hash__())
        f.save(filename,buffer_size=16384)

        data = None
        with open(filename) as jsonFile:
            data = json.load(jsonFile)

        os.remove(filename) # data is saved, get rid of file

        # send it to the db
        try:
            response = DatasetServices().addDataset(data["Dataset"],db)
            response = ResultServices().addResult(data["Result"],db)
            response = ApproachServices().addApproach(data["Approach"],db)

            return response

        except Exception as e:
            return str(e)

    else:
        return 'error'


if __name__ == "__main__":

    app.run()




