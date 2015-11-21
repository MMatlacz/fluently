import json
import sqlite3, urllib
import pyttsx
from contextlib import closing
import os

import time
from flask import Flask, render_template, g, request, url_for, redirect

app_url = '/fluently'
app = Flask(__name__)
app.config.from_pyfile('fluently.ini', silent=False)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_db()
    return db
@app.route('/categories')
def categories():
    return render_template('phrasebook-categories.html')
@app.route('/')
def main_page():
    return render_template('index.html')
@app.route('/wypadki')
def wypadki():
    # tworzenie strony
    cur = get_db().execute('SELECT * FROM phrases WHERE category LIKE "%wypadki%" ORDER BY priority')
    names = list(map(lambda x: x[0], cur.description))
    print(names)
    phrases = []
    for phrase in cur:
        phrases.append(phrase)
    print(phrases)
    return render_template('phrasebook-template.html', phrases=phrases, image = 'fa-plus')
@app.route('/komunikacja')
def komunikacja():
    # tworzenie strony
    cur = get_db().execute('SELECT * FROM phrases WHERE category LIKE "%komunikacja%" ORDER BY priority')
    names = list(map(lambda x: x[0], cur.description))
    print(names)
    phrases = []
    for phrase in cur:
        phrases.append(phrase)
    print(phrases)
    return render_template('phrasebook-template.html', phrases=phrases, category = 'komunikacja', image = 'fa-subway')
@app.route('/nocleg')
def nocleg():
    # tworzenie strony
    cur = get_db().execute('SELECT * FROM phrases WHERE category LIKE "%nocleg%" ORDER BY priority')
    names = list(map(lambda x: x[0], cur.description))
    print(names)
    phrases = []
    for phrase in cur:
        phrases.append(phrase)
    print(phrases)
    return render_template('phrasebook-template.html', phrases=phrases, category = 'nocleg', image = 'fa-bed')
@app.route('/jedzenie')
def jedzenie():
    # tworzenie strony
    cur = get_db().execute('SELECT * FROM phrases WHERE category LIKE "%jedzenie%" ORDER BY priority')
    names = list(map(lambda x: x[0], cur.description))
    print(names)
    phrases = []
    for phrase in cur:
        phrases.append(phrase)
    print(phrases)
    return render_template('phrasebook-template.html', phrases=phrases, category = 'jedzenie', image = 'fa-cutlery')
@app.route('/ogolne')
def ogolne():
    # tworzenie strony
    cur = get_db().execute('SELECT * FROM phrases WHERE category LIKE "%ogolne%" ORDER BY priority')
    names = list(map(lambda x: x[0], cur.description))
    print(names)
    phrases = []
    for phrase in cur:
        phrases.append(phrase)
    print(phrases)
    return render_template('phrasebook-template.html', phrases=phrases, category = 'ogolne', image = 'fa-commenting')

@app.route('/count_phrase', methods=['GET','POST'])
def count_phrase():
    cur = connect_db()
    id = request.args['id']
    category = request.args['c']
    print(id)
    cur.execute("""
    UPDATE phrases
    SET  priority = priority + 1
    WHERE id is
    """ + str(id))
    cur.commit()
    print(request.url_rule)
    url = '/' + category
    return redirect(url)

@app.route('/popular_places', methods=['POST'])
def popular_places():
    cur = connect_db()
    place = request.args['place']
    cur.execute("""
    UPDATE places
    SET popularity = popularity + 1
    WHERE id is
    """ + str(place))
    cur.commit()
    return main_page()

@app.route('/list_popular')
def list_popular():
    cur = get_db().execute('SELECT * FROM places')
    places = []
    for place in cur:
        places.append(place)
    print(places)
    return render_template('places.html', places=places)

@app.route('/get_country', methods=['POST', 'GET'])
def get_country():
    lat = request.args['lat']
    lon = request.args['lon']
    print "costam"
    return main_page()


def write_most_popular_places(localization):
    print("dsaa")
    # baza.write("localization ++")

def voice(lang, text):
    whole =""
    p1 = u"https://translate.google.com/translate_tts?ie=UTF-8&q="
    p2 = urllib.quote_plus(text)
    p3=u"&tl=" + urllib.quote_plus(lang)
    p4=u"&total=1&idx=0&textlen=36&tk=144350.266451&client=t&prev=input&ttsspeed=1"
    whole = p1 + p2 + p3 +p4
    div = '<video controls="" name="media" style="max-width: 100%; max-height: 100%;"><source src="' + whole + '" type="audio/mpeg"></video>'
    return div


if __name__ == '__main__':
    app.run()
