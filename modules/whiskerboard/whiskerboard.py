#!/usr/bin/python -tt
import httplib
import urllib
import json
from datetime import datetime

__author__ = 'Sijis Aviles'


class WhiskerBoard(object):

    default_protocol = 'http'
    default_host = 'localhost'
    default_port = '8080'
    default_user = ('api', 'api')
    default_api = '/api/v1'

    def __init__(self, protocol=default_protocol, host=default_host, port=default_port, api=default_api, user=default_user):

        self.protocol = protocol
        self.host = host
        self.port = port
        self.api = api
        self.user = user[0]
        self.password = user[1]

        self.headers = {
            'Content-type': 'application/json',
            'Accept': '*/*',
        }

    def basic_authorization(self, user, password):
        s = '%s:%s' % (user, password)
        return 'Basic ' + s.encode('base64').rstrip()

    def get_status_uri(self, name):
        data, response = self.connection('GET', '%s/statuses/?name=%s' % (self.api, name), '', self.headers)
        uri = data['objects'][0]['resource_uri']
        return uri

    def get_service_uri(self, name):
        data, response = self.connection('GET', '%s/services/?name=%s' % (self.api, name), '', self.headers)
        uri = data['objects'][0]['resource_uri']
        return uri

    def connection(self, method, url, params, headers):

        conn = httplib.HTTPConnection(self.host, self.port)
        conn.request(method, url, params, headers)
        response = conn.getresponse()

        # POST doesn't return data
        if method.upper() == 'GET':
            data = json.loads(response.read())
        else:
            data = response.read()

        resp = {'status': response.status, 'reason': response.reason}

        return data, resp

    def update_status(self, status, message, service):

        # getting uri
        status = status.capitalize()
        service = service.lower()

        status_uri = self.get_status_uri(status)
        service_uri = self.get_service_uri(service)

        self.headers['Authorization'] = self.basic_authorization(self.user, self.password)

        params = {
            'informational': False,
            'message': '%s' % message,
            'service': '%s' % service_uri,
            'start': '%s' % datetime.now(),
            'status': '%s' % status_uri,
        }

        params = json.dumps(params)
        api_url = '%s/%s/' % (self.api, 'events')

        data, response = self.connection('POST', api_url, params, self.headers)

        return data, response
