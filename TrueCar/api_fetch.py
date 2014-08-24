'''This script requests data from an API in JSON format and then outputs the data into a 
CSV file.'''

from urllib2 import Request, urlopen, URLError
import pandas as pd
import json
import csv

request = Request('http://api.bike-stats.co.uk/service/rest/bikestats?format=json')

try:
    response = urlopen(request)
    bikestats = response.read()
    bikeDict = json.loads(bikestats)
    writer = csv.DictWriter(open('bike_data_20140821.csv', 'w'),['locked','name','emptySlots','longitude','installed','latitude','temporary','@ID','bikesAvailable'],
                        delimiter=',',    # delimiter (separator)
                        extrasaction='ignore')  # ignore columns in the dict if they are skipped

    writer.writeheader()

    for bikeData in bikeDict['dockStation']:
        writer.writerow(bikeData)
except URLError, e:
    print 'Got an error:', e