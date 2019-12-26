"""
    :summary This is python 3.7 supported RPC Microservice Extension with RPC Proxy Dependency

    :since December 2019

    :author Sathya Sai M

    :keyword Python, RPC Microservice

"""
from nameko.rpc import rpc, RpcProxy

class ExpandedGreeterService(object):
    name = 'expanded_greeter_service'

    greeter_service = RpcProxy('greeter_service')

    @rpc
    def greet(self,name):
        """Return an Extended String greeting using the passed name

        Expands on the standard greeting provided by the greeting_service

         :param name: 'str' name of the person to greet

        """

        return '{} Welcome to Pygotham!'.format(
            self.greeter_service.greet(name))
