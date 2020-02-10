# This is Kerry Rainford's Week 2 Assignment

def downloadData(url=str):
    import urllib2
    response = urllib2.urlopen('https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv')
    html = response.read()
