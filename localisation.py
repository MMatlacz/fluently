import pprint, os, pycountry


__author__ = 'Jasiek'
import urllib, json


url = "http://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&sensor=false"
response = urllib.urlopen(url)
data = json.loads(response.read())

country = data['results'][0]['address_components'][6]['long_name']
country_short = data['results'][0]['address_components'][6]['short_name']




print country_short
#print len(pycountry.countries)
#print len(pycountry.languages)
country_object = pycountry.countries.get(alpha2 = country_short)
print(country_object.numeric)
try:
    language = pycountry.languages.get(numeric = country_object.numeric)
    print language.alpha2
    print language.name
except:

    pass
country_full_name = country_object.official_name
print country_full_name
