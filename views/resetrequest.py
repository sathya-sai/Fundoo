"""
    :Summary This is python 3.7 supported fundoo notes application having MySQL 5.7.28 database

    :Since November 2019

    :Author Sathya Sai M

    :keyword Python, MySQL, Python core project, fundoo reset password.

"""
import cgi
import os
from email.mime.multipart import MIMEMultipart

import jwt

from config.settings import mydb_connection
from config.smtp_setup import smtp


def reset_request(self):
    if self.path == '/reset_request':
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        email_id = form['email_id'].value
        print(email_id)
        cursor = mydb_connection.cursor()
        sql = "SELECT  id FROM registration WHERE email_id ='{}'".format(
            email_id)
        cursor.execute(sql)
        x = cursor.fetchall()
        print(len(x), '--------fetchall')
        if len(x) >= 1:
            response = {
                "success": False,
                "message": "something went wrong",
                "data": []
            }
            msg = MIMEMultipart()
            payload = {'id': x[0]}
            key = os.getenv("JWT_SECRET_KEY")
            algorithm = os.getenv("JWT_ALGORITHM")
            token = jwt.encode(payload=payload, key=key, algorithm=algorithm).decode('utf-8')
            print(token)
            message = f"http:(os.getenv('IP')/reset_token/{token}"
            print(message)
            smtp(email_id)
            print("successfully sent email to %s:" % (msg['To']))
            response['success'] = True
            response['message'] = 'sent email if it exist'
            return response