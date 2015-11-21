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
    cur = get_db().execute('SELECT * FROM phrases WHERE category LIKE "%wypadki%" ORDER BY priority DESC')
    names = list(map(lambda x: x[0], cur.description))
    print(names)
    phrases = []
    voices = []
    for phrase in cur:
        phrases.append(phrase)
        voices.append(voice('en-gb', phrase[2]))
    print(phrases)
    return render_template('phrasebook-template.html', data = zip(phrases, voices), category = 'wypadki', image = 'fa-plus')
@app.route('/komunikacja')
def komunikacja():
    # tworzenie strony
    cur = get_db().execute('SELECT * FROM phrases WHERE category LIKE "%komunikacja%" ORDER BY priority DESC')
    names = list(map(lambda x: x[0], cur.description))
    print(names)
    phrases = []
    voices = []
    for phrase in cur:
        phrases.append(phrase)
        voices.append(voice('en-gb', phrase[2]))
    print(phrases)
    return render_template('phrasebook-template.html', data = zip(phrases, voices), category = 'komunikacja', image = 'fa-subway')
@app.route('/nocleg')
def nocleg():
    # tworzenie strony
    cur = get_db().execute('SELECT * FROM phrases WHERE category LIKE "%nocleg%" ORDER BY priority DESC')
    names = list(map(lambda x: x[0], cur.description))
    print(names)
    phrases = []
    voices = []
    for phrase in cur:
        phrases.append(phrase)
        voices.append(voice('en-gb', phrase[2]))
    print(phrases)
    return render_template('phrasebook-template.html', data = zip(phrases, voices), category = 'nocleg', image = 'fa-bed')
@app.route('/jedzenie')
def jedzenie():
    # tworzenie strony
    cur = get_db().execute('SELECT * FROM phrases WHERE category LIKE "%jedzenie%" ORDER BY priority DESC')
    names = list(map(lambda x: x[0], cur.description))
    print(names)
    phrases = []
    voices = []
    for phrase in cur:
        phrases.append(phrase)
        voices.append(voice('en-gb', phrase[2]))
    print(phrases)
    return render_template('phrasebook-template.html', data = zip(phrases, voices), category = 'jedzenie', image = 'fa-cutlery')
@app.route('/ogolne')
def ogolne():
    # tworzenie strony
    cur = get_db().execute('SELECT * FROM phrases WHERE category LIKE "%ogolne%" ORDER BY priority DESC')
    names = list(map(lambda x: x[0], cur.description))
    print(names)
    phrases = []
    voices = []
    for phrase in cur:
        phrases.append(phrase)
        voices.append(voice('en-gb', phrase[2]))
    print(phrases)
    return render_template('phrasebook-template.html', data = zip(phrases, voices), category = 'ogolne', image = 'fa-commenting')
@app.route('/culture')
def culture():
    return render_template('culture.html')

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

def voice(lang, text):
    div = '<video controls="" name="media" style="width: 50%; height: 30px"><source src="http://api.voicerss.org/?key=4d696d0c72a74f5594411d4977c70287&src=' + text + "&amp;hl=" + lang + "&amp;f=48khz_16bit_stereo" + '" type="audio/mpeg"></video>'
    print(div)
    return div


if __name__ == '__main__':
    app.run()
