"""
    @summary Profile Picture Update Connections
    @author Sathya Sai M
    @since November 2019
"""
from config.settings import mydb_connection


def profile_update(image):
    cursor = mydb_connection.cursor()
    sql = "UPDATE picture SET image= '%s' WHERE id='{}'".format(id), image

    val = (id, image)
    try:
        if cursor.execute(sql, val) is None:
            mydb_connection.commit()
            print("SucessFully uploaded")
        else:
            print("Not updated")
    except:
        mydb_connection.rollback()
        mydb_connection.close()