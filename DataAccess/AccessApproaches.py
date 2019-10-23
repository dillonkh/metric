import sqlite3
from sqlite3 import Error

class AccessApproaches:
    
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

    def addApproach(self,approach):
        # create a connection
        conn = self.__createConnection(self.__database)

        if conn is not None:
            # make the insert command
            insert = '''INSERT INTO Approaches 
                        VALUES('{}','{}','{}','{}');
                    '''.format(approach.getName(),approach.getArchDetails(),approach.getPaperLink(),approach.getOwnerID())
            
            dbResponse = self.__execute(conn,insert) # execute it
            
            return dbResponse

        else:
            print("Error! Cannot create the database connection.")
            return "Error! Cannot create the database connection."
