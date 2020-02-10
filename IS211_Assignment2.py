# This is Kerry Rainford's Week 2 Assignment

def downloadData(url=str):
    """This function downloads the contents located at the url and returns it to a caller"""
    import urllib2
    response = urllib2.urlopen('https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv')
    html = response.read()

# do I need to tell the function where to put the file?

def processData():
    """Takes the contents of the file as the first parameter, process the file line by line, and returns
    a dictionary. The dictionary maps a person's ID to a tuple (name, birthday)"""
    
