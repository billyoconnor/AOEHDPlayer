#!/usr/bin/python3
import string, random, json, sys, argparse, time, os
from civAssignHandler import civAssignHandler

def main(numOfPlayers, numOfCivs):
    handler = civAssignHandler(numOfPlayers, numOfCivs)
    handler.execute()


if __name__ == '__main__':
    mainResult = main(5, 18)
    print(mainResult)
