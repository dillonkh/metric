from flask_app import db


class Approach(db.Model):

    __tablename__ = "approaches"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(4096))
    archDetails = db.Column(db.String(4096))
    paperLink = db.Column(db.String(4096))
    ownerID = db.Column(db.String(4096))

    def __init__(self, name,archDetails,paperLink,ownerID):
        self.name = name
        self.archDetails = archDetails
        self.paperLink = paperLink
        self.ownerID = ownerID




        from flask_app import db



