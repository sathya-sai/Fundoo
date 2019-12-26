"""
    :summary This is python 3.7 supported Login, Registration, Reset Password using
     Python Microservices haing MySQL 5.7.28 database and Postman

    :since November 2019

    :author Sathya Sai M

    :keyword Python, MySQL, Python core project, Login, Registration, Reset Password
"""
import os
import smtplib
from email.mime.multipart import MIMEMultipart

import jwt
import simplejson
from nameko.web.handlers import http
from http.server import HTTPServer

from config.settings import mydb_connection


class HttpService(object):
    name = "multiply_service"

    """
            :summary Registration

            :return void
        """


    def register(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        test_data = simplejson.loads(post_body)
        print("post_body(%s)" % test_data)
        json = test_data
        print(json)
        email_id = json['email_id']
        username = json['username']
        password = json['username']
        cursor = mydb_connection.cursor()
        # inserting into the database using sql commands
        sql = "insert into registration (email_id, username, password) values (%s, %s, %s)"
        # The row values are provided in the form of tuple
        val = (email_id, username, password)
        try:
            if cursor.execute(sql, val):
                mydb_connection.commit()
            else:
                mydb_connection.commit()
                val = 1
                if val == 1:
                    # if the data inserted successfull
                    print("reg sucessfull")

                else:
                    # if the data not inserted successfully
                    print("registration failed")
        except:
            mydb_connection.rollback()
            mydb_connection.close()

    """
            :summary Login

            :return void
        """
    @http('GET', '/login')
    def login(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        test_data = simplejson.loads(post_body)
        print("post_body(%s)" % test_data)
        json = test_data
        print(json)
        username = json['username']
        password = json['username']
        cursor = mydb_connection.cursor()
        print(username, password)
        # login and saving to the database using sql commands
        sql = "SELECT  username, password FROM registration WHERE username ='{}' and password ='{}'".format(
            username, password)
        cursor.execute(sql)
        x = cursor.fetchall()
        print(len(x), '--------fetchall')
        # if the user filled the correct details
        if len(x) >= 1:
            print('login success')
        else:
            # if the user filled the wrong details
            print("login failed")

    """
            :summary Forget Password

            :return void
        """
    @http('GET', '/forgetpassword')
    def forget_password(self):
        global response
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        test_data = simplejson.loads(post_body)
        print("post_body(%s)" % test_data)
        json = test_data
        print(json)
        email_id = json['email_id']

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
            payload = {'id': x[0]}
            key = os.getenv("JWT_SECRET_KEY")
            algorithm = os.getenv("JWT_ALGORITHM")
            token = jwt.encode(payload=payload, key=key, algorithm=algorithm).decode('utf-8')
            print(token)
            message = f"http:(os.getenv('IP')/reset_token/{token}"
            print(message)
            msg = MIMEMultipart()
            # setup the parameters of the message
            password = os.getenv("SMTP_EXCHANGE_USER_PASSWORD")
            msg['From'] = os.getenv("SMTP_EXCHANGE_USER_LOGIN")
            msg['To'] = email_id
            msg['Subject'] = "Subscription"
            # add in the message body
            server = smtplib.SMTP('os.getenv("SMTP_EXCHANGE_SERVER"): os.getenv("SMTP_EXCHANGE_PORT")')
            server.starttls()
            # Login Credentials for sending the mail
            server.login(msg['From'], password)
            # send the message via the server.
            server.sendmail(msg['From'], [msg['To']], msg.as_string())
            server.quit()
            print("successfully sent email to %s:" % (msg['To']))
            server.quit()


# server = HTTPServer((os.getenv("SERVER_HOST_IP_ADDRESS"), int(os.getenv('SERVER_HOST_PORT'))), HttpService)
# server.serve_forever()
