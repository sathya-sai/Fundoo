"""
    :summary This is python 3.7 supported Timer Extension microservice

    :since December 2019

    :author Sathya Sai M

    :keyword Python, Timer Extension microservice

"""
from random import choice
from nameko.timer import timer


class PingServices(object):
    name = 'ping_service'

    @timer(interval=1)
    def ping(self):
        """Pings every second"""
        print(choice(['SPAM', 'SPAM', 'EGG', 'BACON', 'SPAMMY SPAM']))
