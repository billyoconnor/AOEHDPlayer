#!/usr/bin/python3
import string, random, json, sys, argparse, time, os, random
from datetime import datetime, timezone, timedelta

class civAssignHandler():

    def __init__(self):
        self.numOfCivs = 18
        self.numOfPlayers = 0
        self.nameofHost = ""
        self.otherPlayerNames = []
        self.expansionList = list(range(1,19))

    def listCreate(self):
        x = range(1, (self.numOfPlayers + 1))
        thisdict = {}
        for i in x:
            thisdict[f'{i}'] = [f'{self.civNumber()}']
        thisdict['1'].append(f"{self.nameofHost}")
        if self.otherPlayerNames:
            y = range(0, (self.numOfPlayers-1))
            for i in y:
                thisdict[f'{i+2}'].append(self.otherPlayerNames[i])
        print("ListCreate Complete")
        print(thisdict)

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
                   '9': 'Saracens',
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
        currentTime = datetime.now()
        currentTime = currentTime.strftime('%Y-%m-%d %H:%M:%S')
        return currentTime

    def execute(self):
        self.log("Starting Execute ")
        print(self.datePrefix)
        print(self.hostName())
        self.expansionCheck()
        print(self.noOfPlayers())
        self.playernames()
        self.listCreate()
        self.log("Execute Complete")

    def hostName(self):
        #Asks name of the person running the request
        hName = input("Enter Host Name ")
        self.nameofHost = hName
        return self.nameofHost


    def log(self, message = None):
        print(f"""[{self.datePrefix}::{message}""")

    def noOfPlayers(self):
        nOP = input("Enter Number of players: ")
        nOP = int(nOP)
        self.numOfPlayers = nOP
        return nOP

    def playernames(self):
        playerNameCheck = input("Would you like to provide player names? Y/N ")
        if playerNameCheck == "Y":
            x = range(2, (self.numOfPlayers + 1))
            for i in x:
                playerName = input(f"Enter name of player {i}: ")
                self.otherPlayerNames.append(playerName)
            return
        else:
            return

    def expansionCheck(self):
        expansionsBoolean = input("Would you like to add expansions to the civ list? Y/N ")
        if expansionsBoolean != 'Y':
            return
        forgottenCheck = input("Would you like to include the expansions for The Forgotten Y/N ")
        if forgottenCheck == 'Y':
            self.expansionList.extend(range(19,24))
        africanKingdomsCheck = input("Would you like to include the expansions for African Kingdoms? Y/N ")
        if africanKingdomsCheck == 'Y':
            self.expansionList.extend(range(24,28))
        rajasCheck = input("Would you like to include the expansions for Rise of the Rajas? Y/N ")
        if rajasCheck == 'Y':
            self.expansionList.extend(range(28,32))
        defintiveCheck = input("Would you like to include the bonus civs from the base DE? Y/N ")
        if defintiveCheck == 'Y':
            self.expansionList.extend(range(32,36))
        lordsCheck = input("Would you like to include the expansions for Lords of the West? Y/N ")
        if lordsCheck == 'Y':
            self.expansionList.extend(range(36,38))
        dukesCheck = input("Would you like to include the expansions for Dawn of the Dukes? Y/N ")
        if dukesCheck == 'Y':
            self.expansionList.extend(range(38,40))
        print(self.expansionList)
        print(f"This is the max value of sampleList: {max(self.expansionList)}")

    def civNumber(self):
        # generates and returns a random number with range
        randNumb = 50
        #setting randNumb to a value outside the range to begin with
        while randNumb not in self.expansionList:
            randNumb = random.randint(1, max(self.expansionList))
        civName = self.civList[f'{randNumb}']
        return civName