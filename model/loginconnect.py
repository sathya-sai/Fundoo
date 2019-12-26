"""
    @summary Logine page connections
    @author Sathya Sai M
    @since November 2019
"""
from config.settings import mydb_connection
from model.open import html_string_success, html_string_logfail

from model.response import Response


def loginconnect(self,username,password):
    cursor = mydb_connection.cursor()
    print(username, password)
    loginconnect(self, username, password)
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