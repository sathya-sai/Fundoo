"""
    :summary This is python 3.7 supported fundooNotes profile picture haing MySQL 5.7.28 database

    :since November 2019

    :author Sathya Sai M

    :keyword Python, MySQL, Python core project, fundooNotes profile picture

"""

import simplejson

from model.profileupdateconnection import profile_update

data = {
    "username": "sathya"
}

"""
    :summary Updating Profile Picture

    :return void
"""


def update_profile(self):
    if self.path == '/profileupdate':
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        test_data = simplejson.loads(post_body)
        print("post_body(%s)" % test_data)
        json = test_data
        print(json)
        json = test_data
        image = json['image']
        profile_update(image)

"""
    :summary Deleting Profile Picture 

    :return void
"""


def delete_profile(self):
    if self.path == '/profiledelete':
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        test_data = simplejson.loads(post_body)
        print("post_body(%s)" % test_data)
        json = test_data
        print(json)
        json = test_data
        id = json['id']
        delete_profile(id)

