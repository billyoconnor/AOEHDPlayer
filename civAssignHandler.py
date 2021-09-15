#!/usr/bin/python3
import string, random, json, sys, argparse, time, os, random

class civAssignHandler(baseClass):

    def __init__(self, requestPayload=None):
        super(civAssignHandler, self).__init__(requestPayload)
        
    @property
    def tableSetsDF(self):
        return self._tableSetsDF

    @tableSetsDF.setter
    def tableSetsDF(self, value):
        self._tableSetsDF = value
        
    @property
    def datePrefix(self):
        now = datetime.utcnow()
        return now

    def execute(self):
        self.logALWAYS("Starting Execute ")
        print(self.datePrefix())
        self.logALWAYS("Execute Complete")

    def civNumber(self, range):
        #generates and returns a random number with range
        randNumb = random.randint(1,18)
        return randNumb 
