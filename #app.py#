# from app import app

import flask
from flask import Flask, request

# from flask_mysqldb import MySQL

import json
import os

# from app import app
app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_DB'] = 'MyDB'

# mysql = MySQL(app)

# from app.Service.DatasetServices import DatasetServices
# from Service.ApproachServices import ApproachServices
# from Service.ResultServices import ResultServices
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
        response = DatasetServices().addDataset(data["Dataset"])
        print("dataset response: {}".format(response))

        response = ApproachServices().addApproach(data["Approach"])
        print("approach response: {}".format(response))

        response = ResultServices().addResult(data["Result"])
        print("result response: {}".format(response))

        return response
    else:
        return 'error'


if __name__ == "__main__":
    
    app.run()

# if __name__ == '__main__':
#     app.run(host='0.0.0.0',port=8080)


