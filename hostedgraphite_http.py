#! /usr/bin/env python3

import urllib.request
from base64 import b64encode

url = "https://hostedgraphite.com/api/v1/sink"
api_key = b'YOUR-API-KEY'
metric = "foo 1.2".encode('utf-8')
headers = {'Authorization': b'Basic ' + b64encode(api_key)}
request = urllib.request.Request(url, metric, headers)
result = urllib.request.urlopen(request) 