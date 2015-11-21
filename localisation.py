# -*- coding: utf-8 -*-
import pprint, os, pycountry, urllib, json, babel
import random

__author__ = 'Jasiek'
pp = pprint.PrettyPrinter(depth=6)


#TODO to powinno byc pobierane przez POSTA
url = "http://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&sensor=false"
response = urllib.urlopen(url)
data = json.loads(response.read())

#wybieranie z danych interesujących nas rzeczy
country = data['results'][0]['address_components'][6]['long_name']
country_short = data['results'][0]['address_components'][6]['short_name']
country_object = pycountry.countries.get(alpha2 = country_short)
country_full_name = country_object.official_name
country_sought_name_iso3 = country_object.alpha3


slowniki = []

komunikaty = {
    'country_name': "Witaj w ",
    'currency': "Tutejsza waluta to ",
    'population': "Tutejsza populacja to ok. ",
    'area': "Obszar kraju w km kw. to ok.",
    'capital': "Stolicą jest ",
}

with open('countryInfo.txt') as infile:
    for line in infile:
        linel = line.split("\t")
        if ((len(linel) > 14) and not (linel[0].startswith('#'))):

            country_name_iso3 = linel[1]
            capital = linel[5]
            area = linel[6]
            population = linel[7]
            currency_name = linel[11]
            languagesli = linel[15].split(",")
            fist = languagesli[0].split("-")[0]
            if fist != '':
                #print fist
                try:
                    lang = pycountry.languages.get(iso639_1_code = fist.name)
                except:
                    lang = ''
                    pass

            slownik = {'country_name': country_name_iso3,'language': languagesli[0], 'langfull': lang, 'currency': currency_name,'population': population, 'area':area, 'capital':capital}
            #print country_name_iso3
            if country_name_iso3 == country_sought_name_iso3:
                print u"Nazwa szukanego języka to: " + languagesli[0]
                #ran=random.randint(0,5)
                key = random.choice(slownik.keys())
                while(key == 'language' or key == 'langfull'):
                    key = random.choice(slownik.keys())

                print komunikaty[key] + slownik[key]


            slowniki.append(slownik)
#pp.pprint(slowniki)