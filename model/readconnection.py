"""
    @summary CRUD operations Read Connection
    @author Sathya Sai M
    @since November 2019
"""
from config.settings import mydb_connection


def read_note():
    cursor = mydb_connection.cursor()
    if mydb_connection.is_connected():
        cursor.execute(" SELECT * FROM crud ")
        # fetch all of the rows from the query
        data = cursor.fetchall()
        print(data)