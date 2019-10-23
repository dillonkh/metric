from Model.Approach import Approach
from DataAccess.AccessApproaches import AccessApproaches


class ApproachServices:

    def __init__(self):
        pass


    def addApproach(self, data, db):
        try:
            # model the data
            approach = Approach(data["name"],data['archDetails'],data["paperLink"],data["ownerID"])

            # Access the DB
            db.session.add(approach)

            db.session.commit()

            return "ok"

        except Exception as e:
            return "error"


