# import sqlite3
# from sqlite3 import Error


# def createConnection(dbFile):
#     """ create a database connection to the SQLite database
#         specified by db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#     conn = None
#     try:
#         conn = sqlite3.connect(dbFile)
#         return conn

#     except Error as e:
#         print(e)

#     return conn


# def createTable(conn, createTableSQL):
#     """ create a table from the create_table_sql statement
#     :param conn: Connection object
#     :param create_table_sql: a CREATE TABLE statement
#     :return:
#     """
#     try:
#         c = conn.cursor()
#         c.execute(createTableSQL)

#     except Error as e:
#         print(e)


# def dropTable(conn, dropTableSQL):
#     try:
#         c = conn.cursor()
#         c.execute(dropTableSQL)

#     except Error as e:
#         print(e)
import flask
from flask import Flask, request

# from app import app
app = Flask(__name__)

# def main():

    # database = "data.db"

    # createDatasets = """ CREATE TABLE Datasets(
    #                         name TEXT,
    #                         numClasses INTEGER,
    #                         numImages INTEGER,
    #                         url TEXT,
    #                         paper TEXT
    #                     ); """ # TODO: missing the paper for test purposes.

    # createApproaches = """CREATE TABLE Approaches(
    #                         name TEXT NOT NULL,
    #                         archDetails TEXT NOT NULL,
    #                         paperLink TEXT NOT NULL,
    #                         ownerID TEXT NOT NULL
    #                     );"""

    # createResults = """CREATE TABLE Results(
    #                         datasetID TEXT NOT NULL,
    #                         approachID TEXT NOT NULL,
    #                         dateSubmitted TEXT NOT NULL,
    #                         trainingDetails TEXT NOT NULL,
    #                         predictionsBlob TEXT NOT NULL
    #                     );""" # TODO: blob should be a blob, not text

    # createUsers = """CREATE TABLE Users(
    #                         username TEXT NOT NULL,
    #                         password TEXT NOT NULL,
    #                         email TEXT NOT NULL
    #                     );"""

    # # create a database connection
    # conn = createConnection(database)

    # # create tables
    # if conn is not None:

    #     # create Results table
    #     dropTable(conn, "DROP TABLE IF EXISTS Users;")
    #     createTable(conn, createUsers)

    #     # create Approaches table
    #     dropTable(conn, "DROP TABLE IF EXISTS Approaches;")
    #     createTable(conn, createApproaches)

    #     # create Datasets table
    #     dropTable(conn, "DROP TABLE IF EXISTS Datasets;")
    #     createTable(conn, createDatasets)

    #     # create Results table
    #     dropTable(conn, "DROP TABLE IF EXISTS Results;")
    #     createTable(conn, createResults)

    # else:
    #     print("Error! cannot create the database connection.")


# if __name__ == '__main__':
#     main()