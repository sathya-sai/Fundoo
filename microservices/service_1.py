"""
    :summary This is python 3.7 supported HTTP Microservice for GET Extension that multiply two numbers

    :since December 2019

    :author Sathya Sai M

    :keyword Python, HttpService GET Method

"""
import json
from nameko.web.handlers import http


class HttpService(object):
    name = "multiply_service"

    # passing numbers to the multiply
    @http('GET', '/multiply/<int:first>/<int:second>')
    def get_method(self, request, first, second):
        third = int(request.args.get('third', 1))

        return json.dumps({'value': first * second * third})
