#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This is Kerry Rainford's Week 2 Assignment

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("url", help = "url to obtain data from amazon", type=str)
args = parser.parse_args()

import logging
logging.basicConfig(filename = "error.log",
                    level = logging.ERROR,
                    filemode = 'w')
assignment2 = logging.getLogger()

def downloadData(url=str):
    """This function downloads the contents located at the url and returns it to a caller"""
    import urllib2
    response = urllib2.urlopen(url)
    html = response.read()
    return html

from datetime import date
import time
def processData(html):
    """Takes the contents of the file as the first parameter, process the file line by line, and returns
    a dictionary. The dictionary maps a person's ID to a tuple (name, birthday)"""
    kerrylinebyline = html.split("\n")

    kerrydict = {}

    for x in range(1, len(kerrylinebyline)-1):
        ktempsplit = kerrylinebyline[x].split(',')

        ktempdate = ktempsplit[2].split("/")

        try:
            kerrydict[int(ktempsplit[0])] = (ktempsplit[1], date(int(ktempdate[2]), int(ktempdate[1]), int(ktempdate[0])))
        except:
            assignment2.error("Error processing line# %d for ID# %s" %(x,ktempsplit[0]))
    return kerrydict

def displayPerson(id=int, personData={}):
    """This function prints the name and birthday of a given user identified by the input ID"""
    dateStr = ("%d-%d-%d" %(personData[id][1].year,personData[id][1].month,personData[id][1].day))
    print("Person #%d is %s with a birthday of %s" %(id,personData[id][0],dateStr))

def main():
    try:
        csvData = downloadData(args.url)
    except:
        assignment2.error("There is a problem with the URL")
    personData = processData(csvData)

    search_for_id = raw_input("Please enter the Lookup ID:")
    while int(search_for_id) >0:
        displayPerson(int(search_for_id), personData)
        search_for_id = raw_input("Please enter the Lookup ID:")

if __name__ == "__main__":
    main()
