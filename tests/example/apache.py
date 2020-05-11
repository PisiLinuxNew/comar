#!/usr/bin/python3
# -*- coding: utf-8 -*-

MSG = {
    'en': 'Hello',
    'tr': 'Merhaba',
}

def info():
    call("apache", "System.Service", "start")
    return "a", "b", "c"

def start():
    notify("System.Service", "Changed", (script(), "started"))
    print(_(MSG))
