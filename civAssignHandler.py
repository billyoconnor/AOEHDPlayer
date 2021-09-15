#!/usr/bin/python3
import string, random, json, sys, argparse, time, os, random
from datetime import datetime, timezone, timedelta

class civAssignHandler():

    def __init__(self, numOfPlayers, numOfCivs):
        self.numOfPlayers = numOfPlayers
        self.numOfCivs = numOfCivs

    def listCreate(self):
        x = range(1, (self.numOfPlayers + 1))
        thisdict = {}
        for i in x:
            thisdict[f'{i}'] = f'{self.civNumber()}'
        return thisdict

    @property
    def tableSetsDF(self):
        return self._tableSetsDF

    @property
    def civList(self):
        civListDict = {'1': 'British',
                   '2': 'Franks',
                   '3': 'Goths',
                   '4': 'Teutons',
                   '5': 'Japanese',
                   '6': 'Chinese',
                   '7': 'Byzantines',
                   '8': 'Persians',
                   '9': 'Sarcens',
                   '10': 'Turks',
                   '11': 'Vikings',
                   '12': 'Mongols',
                   '13': 'Celts',
                   '14': 'Spanish',
                   '15': 'Aztecs',
                   '16': 'Mayans',
                   '17': 'Huns',
                   '18': 'Koreans',
                   '19': 'Italians',
                   '20': 'Indians',
                   '21': 'Incas',
                   '22': 'Magyars',
                   '23': 'Slavs',
                   '24': 'Portuguese',
                   '25': 'Ethiopians',
                   '26': 'Malians',
                   '27': 'Berbers',
                   '28': 'Khmer',
                   '29': 'Malay',
                   '30': 'Burmese',
                   '31': 'Vietnamese',
                   '32': 'Bulgarians',
                   '33': 'Tatars',
                   '34': 'Cumans',
                   '35': 'Lithuanians',
                   '36': 'Burgundians',
                   '37': 'Silicians',
                   '38': 'Poles',
                   '39': 'Bohemians'}
        return civListDict

    @tableSetsDF.setter
    def tableSetsDF(self, value):
        self._tableSetsDF = value
        
    @property
    def datePrefix(self):
        currentTime = datetime.now(timezone.utc)
        return currentTime

    def execute(self):
        self.log("Starting Execute ")
        print(self.datePrefix)
        print(self.listCreate())
        self.log("Execute Complete")

    def civNumber(self):
        #generates and returns a random number with range
        randNumb = random.randint(1,18)
        civName = self.civList[f'{randNumb}']
        return civName

    def log(self, message = None):
        print(f"""[{self.datePrefix}::{message}""")




