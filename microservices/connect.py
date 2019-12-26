"""
    :summary This is python 3.7 supported Database Connection MySQL 5.7.28 database and Postman

    :since November 2019

    :author Sathya Sai M

    :keyword Python, MySQL, Python core project

"""
from sqlalchemy import create_engine


db_url = create_engine("mysql://root:sathyapwd@localhost/fundoo",echo=True)
engine = create_engine(db_url)
conn = engine.connect

try:
    print('your connection is ok \n connecting object is:{}'.format(conn))
except:
    print('not connected')