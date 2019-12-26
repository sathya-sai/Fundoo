"""
    :Summary This is python 3.7 supported fundoo Registration having MySQL 5.7.28 database

    :Since November 2019

    :Author Sathya Sai M

    :keyword Python, MySQL, Python core project, fundoo registration.

"""
import cgi

from model.regconnect import regconnect


def register(self):
    if self.path == '/register':
        # processing user input submitted in Front end(HTML)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        # getting the data
        print(form)
        print(form['email_id'])
        print(form['username'])
        print(form['password'])
        email_id = form['email_id'].value
        username = form['username'].value
        password = form['password'].value
        regconnect(self, email_id, username, password)
