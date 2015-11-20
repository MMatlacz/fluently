import pprint, os, pycountry, urllib, json, babel
__author__ = 'Jasiek'


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


kraje = list(pycountry.countries)
pp = pprint.PrettyPrinter(depth=1)
#pp.pprint(kraje)
cc={}
for country in kraje:
    cc[country.alpha2]=country.name

#pp.pprint(cc)

print cc['EN']
#aragonese = pycountry.languages.get('an')
#print aragonese.name
try:
    print "tutaj try"
    #print country_object.numeric
    #print country_object.alpha2
    language = pycountry.languages.get(iso639_1_code = 'an')
    #print language.alpha2
    #print language.alpha2
    print language.common_name
except:
    pass
country_full_name = country_object.official_name
#print country_full_name
