from Model.Result import Result
from DataAccess.AccessResults import AccessResults


class ResultServices:

    def __init__(self):
        pass


    def addResult(self, data, db):

        try:
            # model the data
            result = Result(data["datasetID"],data["approachID"],data["dateSubmitted"],data["trainingDetails"],data["predictionsBlob"])

            # Access the DB
            db.session.add(result)

            db.session.commit()

            return "ok"

        except Exception as e:
            return "error"
