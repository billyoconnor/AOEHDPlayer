#!/usr/bin/python3
import string, random, json, sys, argparse, time, os
from civAssignHandler import civAssignHandler

def main():
    handler = civAssignHandler()
    handler.execute()


if __name__ == '__main__':
    mainResult = main()
    print(mainResult)
