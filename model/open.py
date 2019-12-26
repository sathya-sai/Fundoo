"""
    :Summary This is python 3.7 supported fundoo notes application having MySQL 5.7.28 database

    :Since November 2019

    :Author Sathya Sai M

    :keyword Python, MySQL, Python core project, fundoo html files.

"""
with open('template/login.html', 'r') as f:
    html_string_login = f.read()

with open('template/register.html', 'r') as f:
    html_string_register = f.read()

with open('template/reset_request.html', 'r') as f:
    html_string_password = f.read()

with open('template/regsuc.html', 'r') as f:
    html_string_regsuc = f.read()

with open('template/regfail.html', 'r') as f:
    html_string_regfail = f.read()

with open('template/success.html', 'r') as f:
    html_string_success = f.read()

with open('template/logfail.html', 'r') as f:
    html_string_logfail = f.read()

from model.response import Response


def openfile(self):
    if self.path == '/login':
        Response(self).html_response(status=202, data=html_string_login)

    if self.path == '/register':
        Response(self).html_response(status=202, data=html_string_register)

    if self.path == '/reset_request':
        Response(self).html_response(status=202, data=html_string_password)

    if self.path == '/regsuc':
        Response(self).html_response(status=202, data=html_string_regsuc)

    if self.path == '/regfail':
        Response(self).html_response(status=202, data=html_string_regfail)

    if self.path == '/success':
        Response(self).html_response(status=202, data=html_string_success)

    if self.path == '/logfail':
        Response(self).html_response(status=202, data=html_string_logfail)