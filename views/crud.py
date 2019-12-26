"""
    :summary This is python 3.7 supported CRUD operations haing MySQL 5.7.28 database and Postman

    :since November 2019

    :author Sathya Sai M

    :keyword Python, MySQL, Python core project, CRUD operations

"""


from dotenv import load_dotenv

from model.createconnection import create_note
from model.deleteconnection import delete_note
from model.readconnection import read_note
from model.updateconnection import update_note

load_dotenv()

import simplejson

data = {
    "username": "sathya"
}

"""
    :summary view/Display 

    :return void
"""


def note_view(self):
    print(self.path)
    if self.path == '/view':
        read_note()


"""
    :summary Creating 

    :return void
"""


def note_create(self):
    print(self.path)
    if self.path == '/create':
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        test_data = simplejson.loads(post_body)
        print("post_body(%s)" % test_data)
        json = test_data
        print(json)
        tittle = json['tittle']
        description = json['description']
        color = json['color']
        isPinned = json['isPinned']
        isArchive = json['isArchive']
        isTrash = json['isTrash']
        create_note(tittle, description, color, isPinned, isArchive, isTrash)


"""
    :summary Updating
    :return void
"""


def note_update(self):
    print(self.path)
    if self.path == '/put':
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        test_data = simplejson.loads(post_body)

        print("post_body(%s)" % (test_data))
        json = test_data
        print(json)
        isPinned = json['isPinned']
        isArchive = json['isArchive']
        update_note(isPinned, isArchive)


"""
    :summary Deleating

    :return void
"""


def note_delete(self):
    print(self.path)
    if self.path == '/delete':
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        test_data = simplejson.loads(post_body)

        print("post_body(%s)" % test_data)
        json = test_data
        print(json)
        print(json['id'])

        id = json['id']
        delete_note(id)


