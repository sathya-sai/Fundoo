"""
    @summary Profile Picture Delete Connections
    @author Sathya Sai M
    @since November 2019
"""
from config.settings import mydb_connection


def delete_profile(id):
    sql = "DELETE from picture WHERE id ={}".format(id)
    cursor = mydb_connection.cursor()
    val = id
    try:
        if cursor.execute(sql, val) is None:
            mydb_connection.commit()
            print("SuccessFully Deleted")
        else:
            print("Not Deleted")
    except:

        mydb_connection.rollback()
        mydb_connection.close()