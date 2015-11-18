# -*- encoding: utf-8 -*-

import os
import xml.etree.ElementTree as ET

def stop():
    command = searchCommand('stop')

    if command != None:
        sendSignal(command)


def cold(temperature):
    command = searchCommand('cold/t' + str(temperature))
    if command == None:
        command = searchCommand('cold/default')

    if command != None:
        sendSignal(command)

def dehum(temperature):
    command = searchCommand('dehum/t' + str(temperature))
    if command == None:
        command = searchCommand('dehum/default')

    if command != None:
        sendSignal(command)

def warm(temperature):
    command = searchCommand('warm/t' + str(temperature))
    if command == None:
        command = searchCommand('warm/default')

    if command != None:
        sendSignal(command)

def sendSignal(command):
    os.system('irsend send_once ac ' + command)

def searchCommand(path):
    tree = ET.parse('./commands.xml')
    root = tree.getroot()
    command = root.find(path).text

    if command != None:
        return command
    else:
        return None
