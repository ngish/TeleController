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
        request_uri = self._endpoint + "lights/latest.json"
        return self._request(request_uri)

    def _request(self, uri):
        http_client = httplib2.Http(".cache")

        resp, content = http_client.request(uri, "GET")
        return self._deserialize(content)

    def _deserialize(self, content):
        return json.loads(content)

    def updateStatus(self, id):
        request_uri = self._endpoint + "lights/" + str(id) + "/update"
        data = {'status':"updated"}
        http_client = httplib2.Http(".cache")
        resp, content = http_client.request(request_uri, "POST", urlencode(data))

def sendSignal(ac_type, temperature):
    if light_type == "Full":
        light_commands.full()
    if light_type == "White":
        light_commands.white()
    if light_type == "Warm":
        light_commands.warm()
    if light_type == "EcoNavi":
        light_commands.econavi()
    if light_type == "On":
        light_commands.on()
    if light_type == "Off":
        light_commands.off()

def initializeLirc():
    import os
    os.system('sudo /etc/init.d/lirc start')

if __name__='__main__':

    import light_commands
    client = RestClient()
    response_entity = client.getLatest()

    status = response_entity["status"]
    print "===Room Light==="
    print "Type:", response_entity["light_type"]
    print "Status:" , status
    if status == "updating":
        initializeLirc()
        sendSignal(response_entity["light_type"])
        client.updateStatus(response_entity["id"])
