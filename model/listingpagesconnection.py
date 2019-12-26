"""
    :summary This is python 3.7 supported listing pages for notes haing MySQL 5.7.28 database and Postman

    :since November 2019

    :author Sathya Sai M

    :keyword Python, MySQL, Python core project, Listing pages for notes

"""
from config.settings import mydb_connection

"""
    :summary isArchive

    :return void
"""


def is_Archive(self):
    print(self.path)
    if self.path == '/isArchive':
        cursor = mydb_connection.cursor()
        if mydb_connection.is_connected():
            cursor.execute("select * from crud where isArchive=1;")
            # fetch all of the rows from the query
            data = cursor.fetchall()
            print(data)


"""
    :summary isPinned

    :return void
"""


def is_Pinned(self):
    print(self.path)
    if self.path == '/isPinned':
        cursor = mydb_connection.cursor()
        if mydb_connection.is_connected():
            cursor.execute("select * from crud where isPinned=1;")
            # fetch all of the rows from the query
            data = cursor.fetchall()
            print(data)


"""
   :summary isTrash

   :return void
"""


def is_Trash(self):
    print(self.path)
    if self.path == '/isTrash':
        cursor = mydb_connection.cursor()
        if mydb_connection.is_connected():
            cursor.execute("select * from crud where isTrash=1;")
            # fetch all of the rows from the query
            data = cursor.fetchall()
            print(data)
