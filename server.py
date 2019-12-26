"""
    :Summary This is python 3.7 supported fundoo notes application having MySQL 5.7.28 database

    :Since November 2019

    :Author Sathya Sai M

    :keyword Python, MySQL, Python core project, fundoo notes.

"""
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

from model.listingpagesconnection import is_Archive, is_Pinned, is_Trash
from views.profilepic import update_profile, delete_profile
from views.crud import note_delete, note_update, note_create, note_view
from views.login import login
from model.open import openfile
from views.register import register
from views.resetrequest import reset_request

data = {
    "username": "sathya"
}


class ServiceHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)

    def _html(self, message):
        content = message
        return content.encode("utf8")

    def do_GET(self):
        openfile(self)
        note_view(self)

    def do_POST(self):
        register(self)
        login(self)
        reset_request(self)
        note_create(self)
        is_Pinned(self)

    def do_DELETE(self):
        note_delete(self)
        delete_profile(self)

    def do_PUT(self):
        note_update(self)
        is_Archive(self)
        is_Trash(self)
        update_profile(self)

server = HTTPServer((os.getenv("SERVER_HOST_IP_ADDRESS"), int(os.getenv('SERVER_HOST_PORT'))), ServiceHandler)
server.serve_forever()


