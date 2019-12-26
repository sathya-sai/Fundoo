"""
    :summary This is python 3.7 supported Event publisher using rpc extension

    :since December 2019

    :author Sathya Sai M

    :keyword Python, Event Handler Extension

"""
from nameko.events import event_handler


class MyEventHandlerServiceOne(object):
    name = 'my_event_handler_service_1'

    @event_handler('my_event_publisher_service', 'my_event')
    def publish(self, payload):
        """Handle a "my_event" payload

        :param payload: 'str' payload to handle

        """

        print("Received an event:{}".format(payload))


class MyEventHandlerServiceTwo(object):
    name = 'my_event_handler_service_2'

    @event_handler('my_event_publisher_service', 'my_event')
    def publish(self, payload):
        """Also handle a "my_event" payload

        :param payload: 'str' payload to handle

        """
        print("Received an event:{}".format(payload))
