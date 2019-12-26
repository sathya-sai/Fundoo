"""
    :summary This is python 3.7 supported RPC Microservice for RPC Remote Procedure Call Extension

    :since December 2019

    :author Sathya Sai M

    :keyword Python, RPC Microservice

"""
from nameko.rpc import rpc


class GreeterService(object):
    name = 'greeter_service'

    @rpc
    def greet(self, name):
        """Return a string greeting using the passed name

        :param name: 'str' name of the persi=on to greet

        """
        return u'Hello {}!'.format(name)
