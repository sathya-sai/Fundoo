"""
    @summary CRUD operation Create Connections
    @author Sathya Sai M
    @since November 2019
"""
from config.settings import mydb_connection


def create_note(tittle,description,color,isPinned,isArchive,isTrash):
    cursor = mydb_connection.cursor()
    sql = "insert into crud (tittle, description, color,isPinned,isArchive,isTrash) values (%s, %s, %s,%s,%s," \
          "%s) "
    # The row values are provided in the form of tuple
    val = (tittle, description, color, isPinned, isArchive, isTrash)
    try:
        if cursor.execute(sql, val) is None:
            mydb_connection.commit()
            print("SucessFully Created")
            breakpoint()
        else:
            print("Not Created")
    except:
        mydb_connection.rollback()
        mydb_connection.close()
