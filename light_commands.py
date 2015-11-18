#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import xml.etree.ElementTree as ET

def full():
    sendSignal('full')

def white():
    sendSignal('white')

def warm():
    sendSignal('warm')

def econavi():
    sendSignal('econavi')

def on():
    sendSignal('on')

def off():
    sendSignal('off')

def sendSignal(command):
    _command = searchCommand(command)
    if _command != None:
        _sendSignal(_command)

def _sendSignal(command):
    os.system('irsend send_once light ' + command)

def searchCommand(path):
    tree = ET.parse('./light_commands.xml')
    root = tree.getroot()
    command = root.find(path).text
    default = root.find('default').text

    if command != None:
        return command
    else:
        return None
