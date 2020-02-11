#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This is Kerry Rainford's Week 2 Assignment

def downloadData(url=str):
    """This function downloads the contents located at the url and returns it to a caller"""
    import urllib2
    response = urllib2.urlopen('https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv')
    html = response.read()
    return html

#downloadData()

from datetime import date
import time
def processData(html):
    """Takes the contents of the file as the first parameter, process the file line by line, and returns
    a dictionary. The dictionary maps a person's ID to a tuple (name, birthday)"""
    kerrylinebyline = html.split("\n")
    #print(kerrylinebyline)

    kerrydict = {}

    for x in range(1, len(kerrylinebyline)-1):
        ktempsplit = kerrylinebyline[x].split(',')

        ktempdate = ktempsplit[2].split("/")
        #print(ktempsplit)
        #print(ktempdate)

        try:
            kerrydict[int(ktempsplit[0])] = (ktempsplit[1], date(int(ktempdate[2]), int(ktempdate[1]), int(ktempdate[0])))
        except:
            print("Error on line %d", x)
    print(kerrydict)

import logging
KERRY_LOGFORM = "Error processing line %(lineno)d for ID# %d"
logging.basicConfig(filename = "assignment2.log",
                    level = logging.ERROR,
                    format = KERRY_LOGFORM,
                    filemode = 'w')
logger = logging.getLogger()

def displayPerson(id=int, personData={}):
    """This function prints the name and birthday of a given user identified by the input ID"""
    #print()

processData(downloadData())
