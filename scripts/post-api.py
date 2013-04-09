#!/usr/bin/python -tt
import httplib
import urllib
import json


def basic_authorization(user, password):
    s = '%s:%s' % (user, password)
    return "Basic " + s.encode('base64').rstrip()

params = {
    "informational": False,
    "message": "new message 7",
    "service": "/api/v1/services/1/",
    "start": "2012-11-26T03:58:01",
    "status": "/api/v1/statuses/1/",
}

params = json.dumps(params)

headers = {
    'Content-type': 'application/json',
    'Authorization': basic_authorization('api', 'api'),
    'Accept': '*/*',
    'User-Agent': 'curl/7.24.0 (x86_64-redhat-linux-gnu) libcurl/7.24.0 NSS/3.13.3.0 zlib/1.2.5 libidn/1.24 libssh2/1.4.1',
}

conn = httplib.HTTPConnection('localhost', '8000')
conn.set_debuglevel(1)
#conn.request('GET', '/api/v1/services/', '', headers)
conn.request('POST', '/api/v1/events/', params, headers)
response = conn.getresponse()
data = response.read()
print response.status, response.reason
print data
