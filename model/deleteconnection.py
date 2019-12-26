"""
    @summary CRUD operations Delete connections
    @author Sathya Sai M
    @since November 2019
"""
from config.settings import mydb_connection


def delete_note(id):
    cursor = mydb_connection.cursor()
    sql = "DELETE from crud WHERE id ='{}'".format(id)

    # The row values are provided in the form of tuple
    val = id
    try:
        if cursor.execute(sql, val) is None:
            mydb_connection.commit()
            print("SucessFully Deleted")
        else:
            print("Not Deleted")
    except:
        mydb_connection.rollback()
        mydb_connection.close()