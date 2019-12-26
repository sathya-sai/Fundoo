"""
    @summary CRUD operation Update connection
    @author Sathya Sai M
    @since November 2019
"""
from config.settings import mydb_connection


def update_note(isPinned,isArchive):
    cursor = mydb_connection.cursor()
    sql = "UPDATE crud SET isPinned= '%s', isArchive = '%s',  WHERE id = 6"
    # The row values are provided in the form of tuple
    val = (isPinned, isArchive)

    try:
        if cursor.execute(sql, val) is None:
            mydb_connection.commit()
            print("updated successfully")
        else:
            print("update failed")


    except:
        mydb_connection.rollback()
        mydb_connection.close()