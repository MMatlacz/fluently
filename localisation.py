import pprint, os, pycountry, urllib, json, babel
__author__ = 'Jasiek'


url = "http://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&sensor=false"
response = urllib.urlopen(url)
data = json.loads(response.read())

country = data['results'][0]['address_components'][6]['long_name']
country_short = data['results'][0]['address_components'][6]['short_name']
country_object = pycountry.countries.get(alpha2 = country_short)
country_full_name = country_object.official_name

with open('countryInfo.txt') as infile:
    for line in infile:
        linel = line.split("\t")
        if len(linel) > 12:
            print linel




