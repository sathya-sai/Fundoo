"""
    :summary This is python 3.7 supported Event publisher using rpc extension

    :since December 2019

    :author Sathya Sai M

    :keyword Python, Event Dispatcher Microservice

"""
from nameko.events import EventDispatcher
from nameko.rpc import rpc


class MyEventPublisherService(object):
    name = 'my_event_publisher_service'

    dispatch = EventDispatcher()

    @rpc
    def publish(self, payload):
        """Publish an event with the passed payload

        param payload: 'str' payload to publish with the Event

        """
        self.dispatch('my_event', payload)
 