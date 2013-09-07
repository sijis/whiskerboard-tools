#!/usr/bin/python -tt

import urllib2
import simplejson
import sys
import pprint

try:
    url = sys.argv[1]
except Exception as e:
    url = 'http://localhost:8000/api/v1/services/?format=json'

req = urllib2.Request(url, None, {'content-type': 'application/json'})
opener = urllib2.build_opener()
f = opener.open(req)
output = simplejson.load(f)

print 'URL: %s' % url
pprint.pprint(output)
