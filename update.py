#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import httplib2
from urllib import urlencode
import json

command_path="."
class RestClient(object):

    def __init__(self):
        self._endpoint = "{server url}"
        self._format = "json"

    def getLatest(self):
        request_uri = self._endpoint + "conditions/latest.json"
        return self._request(request_uri)

    def _request(self, uri):
        http_client = httplib2.Http(".cache")

        resp, content = http_client.request(uri, "GET")
        return self._deserialize(content)

    def _deserialize(self, content):
        return json.loads(content)

    def updateStatus(self, id):
        request_uri = self._endpoint + "conditions/" + str(id) + "/update"
        data = {'status':"updated"}
        http_client = httplib2.Http(".cache")
        resp, content = http_client.request(request_uri, "POST", urlencode(data))

def sendSignal(ac_type, temperature):
    if ac_type == "Cooler":
        commands.cold(temperature)
    elif ac_type == "Warmer":
        commands.warm(temperature)
    elif ac_type == "Dehum":
        commands.dehum(temperature)
    elif ac_type == "Stop":
        comamnds.stop()

def initializeLirc():
    import os
    os.system('sudo /etc/init.d/lirc start')

if __name__='__main__':

    import commands
    client = RestClient()
    response_entity = client.getLatest()

    status = response_entity["status"]

    print "===Air Conditioner==="
    print "Type:", response_entity["ac_type"]
    print "Temperature:", response_entity["temperature"]
    print "Status:" , status
    if status == "updating":
        initializeLirc()
        sendSignal(response_entity["ac_type"], response_entity["temperature"])
        client.updateStatus(response_entity["id"])
