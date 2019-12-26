"""
    :Summary This is python 3.7 supported fundoo Login having MySQL 5.7.28 database

    :Since December 2019

    :Author Sathya Sai M

    :keyword Python, MySQL, Python core project, fundoo login.

"""
import cgi

from config.settings import mydb_connection
from model.loginconnect import loginconnect
from model.open import html_string_success, html_string_logfail
from model.response import Response


def login(self):
    if self.path == '/login':
        self._html("hi!")
        # processing user input submitted in Front end(HTML)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        # getting the username and password
        username = form['username'].value
        password = form['password'].value
        cursor = mydb_connection.cursor()
        print(username, password)
        # loginconnect(self, username, password)
        # login and saving to the database using sql commands
        sql = "SELECT  username, password FROM registration WHERE username ='{}' and password ='{}'".format(
            username, password)
        cursor.execute(sql)
        x = cursor.fetchall()
        print(len(x), '--------fetchall')
        # if the user filled the correct details
        if len(x) >= 1:
            Response(self).html_response(status=202, data=html_string_success)
            print('success')
        else:
            # if the user filled the wrong details
            print("login failed")
            Response(self).html_response(status=202, data=html_string_logfail)
