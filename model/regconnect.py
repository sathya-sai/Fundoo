"""
    @summary Registration Connections
    @author Sathya Sai M
    @since November 2019
"""

from config.settings import mydb_connection
from model.open import html_string_regsuc, html_string_regfail

from model.response import Response


def regconnect(self,email_id,username,password):
    cursor = mydb_connection.cursor()
    # inserting into the database using sql commands
    sql = "insert into registration (email_id, username, password) values (%s, %s, %s)"
    # The row values are provided in the form of tuple
    val = (email_id, username, password)
    try:
        if cursor.execute(sql, val) is None:
            mydb_connection.commit()
            Response(self).html_response(status=202, data=html_string_regsuc)
            print("reg sucessfull")
        else:
            Response(self).html_response(status=202, data=html_string_regfail)
            print("registration failed")
    except:
        mydb_connection.rollback()
        mydb_connection.close()