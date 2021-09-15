#!/usr/bin/python3
import string, random, json, sys, argparse, time, os

def main(event, context):
    handler = civAssignHandler()
    handler.execute()


## executing locally we are not passing in any events
if __name__ == '__main__':
    mainResult = main(None, None)
    print(json.dumps(mainResult,indent=2))
