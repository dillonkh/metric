import sqlite3
from sqlite3 import Error

class AccessResults:
    
    __database = "Database/data.db"

    def __init__(self):
        pass

    def __createConnection(self, dbFile):
        
        conn = None
        try:
            conn = sqlite3.connect(dbFile)
            return conn

        except Error as e:
            print(e)
    
        return conn

    def __execute(self,conn,command):
        try:
            c = conn.cursor()
            c.execute(command)
            conn.commit()

            return "Added Successfully!"

        except Error as e:
            return e

    def addResult(self,result):
        # create a connection
        conn = self.__createConnection(self.__database)

        if conn is not None:
            # make the insert command
            insert = '''INSERT INTO Results 
                        VALUES('{}','{}','{}','{}','{}');
                    '''.format(result.getDatasetID(),result.getApproachID(),result.getDateSubmitted(),result.getTrainingDetails(),result.getPredictionsBlob())
            
            dbResponse = self.__execute(conn,insert) # execute it
            
            return dbResponse

        else:
            print("Error! Cannot create the database connection.")
            return "Error! Cannot create the database connection."
