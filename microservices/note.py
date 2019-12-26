"""
    :summary This is python 3.7 supported CRUD operations using HTTP Microsevices haing MySQL 5.7.28 database and Postman

    :since November 2019

    :author Sathya Sai M

    :keyword Python, MySQL, Python core project, CRUD operations, HTTP Microservices

"""
import os
from http.server import HTTPServer

import simplejson
from nameko.web.handlers import http

from config.settings import mydb_connection


class HttpService(object):
    name = "multiply_service"

    def __init__(self):
        self.rfile = None
        self.headers = None
        self.path = None

    """
        :summary CREATE

        :return void
    """

    @http('GET', '/create')
    def create(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        test_data = simplejson.loads(post_body)
        print("post_body(%s)" % test_data)
        json = test_data
        print(json)
        print(json['tittle'])
        tittle = json['tittle']
        description = json['description']
        color = json['color']
        isPinned = json['isPinned']
        isArchive = json['isArchive']
        isTrash = json['isTrash']
        # print(tittle, description, color, isPinned, isArchive, isTrash)
        cursor = mydb_connection.cursor()
        sql = "insert into crud (tittle, description, color,isPinned,isArchive,isTrash) values (%s, %s, %s,%s,%s," \
              "%s) "
        # The row values are provided in the form of tuple
        val = (tittle, description, color, isPinned, isArchive, isTrash)
        try:
            if cursor.execute(sql, val):
                mydb_connection.commit()
            else:
                mydb_connection.commit()
                val = 1
                if val == 1:
                    print("SucessFully Created")
                    breakpoint()
                else:
                    print("Not Created")
        except:
            mydb_connection.rollback()
            mydb_connection.close()

    """
        :summary READ

        :return void
    """

    @http('GET', '/read')
    def read(self):
        cursor = mydb_connection.cursor()
        if mydb_connection.is_connected():
            cursor.execute(" SELECT * FROM crud ")
            # fetch all of the rows from the query
            data = cursor.fetchall()
            print(data)

    """
        :summary UPDATE

        :return void
    """

    @http('GET', '/update')
    def update(self):

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        test_data = simplejson.loads(post_body)

        print("post_body(%s)" % (test_data))
        json = test_data
        print(json)
        isPinned = json['isPinned']
        isArchive = json['isArchive']

        print(id, isPinned, isArchive)

        cursor = mydb_connection.cursor()
        sql = "UPDATE crud SET isPinned= '%s', isArchive = '%s',  WHERE id = 6"
        # The row values are provided in the form of tuple
        val = (isPinned, isArchive)

        try:
            if cursor.execute(sql, val):
                mydb_connection.commit()
            else:
                mydb_connection.commit()
                val = 1
                if val == 1:
                    print("SucessFully updated")
                    breakpoint()
                else:
                    print("Not updated")
        except:
            mydb_connection.rollback()
            mydb_connection.close()

    """
        :summary DELETE

        :return void
    """

    @http('GET', '/delete')
    def delete(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        test_data = simplejson.loads(post_body)

        print("post_body(%s)" % test_data)
        json = test_data
        print(json)
        print(json['id'])

        id = json['id']

        cursor = mydb_connection.cursor()
        sql = "DELETE from crud WHERE id ='{}'".format(id)

        # The row values are provided in the form of tuple
        val = id
        try:
            if cursor.execute(sql, val):
                mydb_connection.commit()
            else:
                mydb_connection.commit()
                val = 1
                if val == 1:
                    print("SuccessFully Deleted")
                else:
                    print("Not Deleted")
        except:
            mydb_connection.rollback()
            mydb_connection.close()


server = HTTPServer((os.getenv('IP'), int(os.getenv('SERVER_HOST_PORT'))), HttpService)
server.serve_forever()

