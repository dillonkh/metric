from flask_app import db


class Result(db.Model):

    __tablename__ = "results"

    id = db.Column(db.Integer, primary_key=True)
    datasetID = db.Column(db.String(4096))
    approachID = db.Column(db.String(4096))
    dateSubmitted = db.Column(db.String(4096))
    trainingDetails = db.Column(db.String(4096))
    predictionsBlob = db.Column(db.String(4096))

    def __init__(self, datasetID,approachID,dateSubmitted,trainingDetails,predictionsBlob):
        self.datasetID = datasetID
        self.approachID = approachID
        self.dateSubmitted = dateSubmitted
        self.trainingDetails = trainingDetails
        self.predictionsBlob = predictionsBlob