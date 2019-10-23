from Model.Dataset import Dataset
from DataAccess.AccessDatasets import AccessDatasets


class DatasetServices:

    def __init__(self):
        pass


    def addDataset(self, data, db):
        try:
            dataset = Dataset(data["name"],data["numClasses"],data["numImages"],data["url"],data["paper"])

            db.session.add(dataset)

            db.session.commit()

            return "ok"

        except Exception as e:
            return "error"
