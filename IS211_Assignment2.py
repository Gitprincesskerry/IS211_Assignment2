#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This is Kerry Rainford's Week 2 Assignment

def downloadData(url=str):
    """This function downloads the contents located at the url and returns it to a caller"""
    import urllib2
    response = urllib2.urlopen('https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv')
    html = response.read()

# do I need to tell the function where to put the file?

import datetime
import time
def processData():
    """Takes the contents of the file as the first parameter, process the file line by line, and returns
    a dictionary. The dictionary maps a person's ID to a tuple (name, birthday)"""

def displayPerson(id=int, personData={}):
    """This function prints the name and birthday of a given user identified by the input ID"""

import logging

logger = logging.getLogger("assignment2.xls")

csvLogger = logging.getLogger("assignment2.csv")
csvLogger.debug("Trying")
csvLogger.warning("File")
csvLogger.error("File unexpected")
csvLogger.critical("File too large")

logger.exception("Error reading file")
logger.error("Error reading file")
logger.log(logging.error, "Error reading file '%s' at offset %d", assignment2.csv, offset, exc_info=1)
