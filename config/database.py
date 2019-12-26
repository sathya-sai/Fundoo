"""
    @summary Database connection details
    @author Sathya Sai M
    @since November 2019
"""
import mysql.connector
import sys


class Database:

    def __init__(self, *args, **kwargs):
        try:
            if type(kwargs) != dict:
                raise Exception("Database connection details not provided")
            else:
                # :todo Fix the member variables
                for key, value in args[0].items():
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

        except:
            if self.mysql.Error:
                print(self.mysql.Error)
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print(sys.exc_info()[2].tb_lineno)
            print('Error: {}. {}, line: {}'.format(sys.exc_info()[0],
                                                   sys.exc_info()[1],
                                                   sys.exc_info()[2].tb_lineno))

    def connect(self):
        mydb_connection = self.mysql.connect(
            host=self.host, database=self.database_name, user=self.username, passwd=self.password)

        return mydb_connection

    def close(self):
        self.mysql.close()
