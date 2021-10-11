#!/usr/bin/python3
import string, random, json, sys, argparse, time, os, cgitb
from civAssignHandler import civAssignHandler

# -*- coding: UTF-8 -*-# enable debugging
cgitb.enable()
print("""Content-Type: text/html;charset=utf-8\n""")
print("Hello World!")

def caller(jdict=None):
    handler = civAssignHandler()
    if jdict is None:
        handler.cmdexecute()
    else:
        handler.jsonexecute(jdict)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        mainResult = caller()
    elif len(sys.argv) == 2:
        loadFile = str(sys.argv[1])
        with open(loadFile, "r") as read_file:
            data = json.load(read_file)
        mainResult = caller(data)


