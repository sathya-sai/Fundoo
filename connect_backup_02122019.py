import mysql.connector
from dotenv import load_dotenv
load_dotenv()


class Database:
    host = None
    database_name = None
    username = None
    password = None

    def __init__(self, *args, **kwargs):
        if type(kwargs) != list:
            raise Exception("Database connection details not provided")

        for key, value in kwargs.items():
            if key == 'host':
                self.host = value
            if key == 'database_name':
                self.database_name = value
            if key == 'username':
                self.username = value
            if key == 'password':
                self.password = value

        self.mysql = mysql.connector
        self.connect()

    def connect(self):
        return self.mysql.connect(
            self.host,
            self.database_name,
            self.username,
            self.password
        )
