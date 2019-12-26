"""
    @summary Settings
    @author Sathya sai M
    @since December 2019
"""

from dotenv import load_dotenv
from config.database import *
import os

load_dotenv()
new = 2


SERVER_HOST_IP_ADDRESS=os.getenv("SERVER_HOST_IP_ADDRESS")
SERVER_HOST_PORT=os.getenv('SERVER_HOST_PORT')


SMTP_CREDENTIALS = {
    "SMTP_EXCHANGE_SERVER":os.getenv("SMTP_EXCHANGE_SERVER"),
    "SMTP_EXCHANGE_PORT":os.getenv("SMTP_EXCHANGE_PORT"),
    "SMTP_EXCHANGE_USER_LOGIN":os.getenv("SMTP_EXCHANGE_USER_LOGIN"),
    "SMTP_EXCHANGE_USER_PASSWORD":os.getenv("SMTP_EXCHANGE_USER_PASSWORD")
}

JWT_SECRET_KEY=os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM=os.getenv("JWT_ALGORITHM")

DATABASE_CREDENTIALS = {
    "host":os.getenv("DATABASE_HOST"),
    "database_name":os.getenv("DATABASE_DATABASE_NAME"),
    "username":os.getenv("DATABASE_USER"),
    "password":os.getenv("DATABASE_PASSWORD")
}

connection_obj = Database(DATABASE_CREDENTIALS).connect()
mydb_connection=connection_obj
