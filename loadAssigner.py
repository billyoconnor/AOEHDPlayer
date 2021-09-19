#!/usr/bin/python3
import string, random, json, sys, argparse, time, os
from civAssignHandler import civAssignHandler

def main(numOfCivs):
    handler = civAssignHandler(numOfCivs)
    handler.execute()


if __name__ == '__main__':
    mainResult = main(18)
    print(mainResult)
