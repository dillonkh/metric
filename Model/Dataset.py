from flask_app import db

class Dataset(db.Model):


    __tablename__ = "datasets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(4096))
    numClasses = db.Column(db.Integer)
    numImages = db.Column(db.Integer)
    url = db.Column(db.String(4096))
    paper = db.Column(db.String(4096))

    def __init__(self, name,numClasses,numImages,url,paper):
        self.name = name
        self.numClasses = numClasses
        self.numImages = numImages
        self.url = url
        self.paper = paper



