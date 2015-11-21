import json
import sqlite3, urllib
from contextlib import closing
import os
from flask import Flask, render_template, g, request

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


@app.route('/phrasebook')
def phrasebook():
    # tworzenie strony
    cur = get_db().execute('SELECT * FROM phrases')
    names = list(map(lambda x: x[0], cur.description))
    print(names)
    phrases = []
    for phrase in cur:
        phrases.append(phrase)
    print(phrases)
    cur.execute("PRAGMA TABLE_INFO('phrases')")
    voice_adres_from_data('polish','hej')
    return render_template('phrasebook-template.html', phrases=phrases)


@app.route('/count_phrase', methods=['POST'])
def countPhrase():
    cur = connect_db()
    id = request.args['id']
    print(id)
    cur.execute("""
    UPDATE phrases
    SET  priority = priority + 1
    WHERE id is
    """ + str(id))
    cur.commit()
    return phrasebook()

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
    return phrasebook()

@app.route('/list_popular')
def list_popular():
    cur = get_db().execute('SELECT * FROM places')
    places = []
    for place in cur:
        places.append(place)
    print(places)
    return render_template('places.html', places=places)


def write_most_popular_places(localization):
    print("dsaa")
    # baza.write("localization ++")

def voice_adres_from_data(lang, text):
    whole =""
    p1 = u"https://translate.google.com/translate_tts?ie=UTF-8&q="
    p2 = urllib.quote_plus(text)
    p3=u"&tl=" + urllib.quote_plus(lang)
    p4=u"&total=1&idx=0&textlen="
    p45=str(len(text))
    p5=u"&tk=144350.266451&client=t&prev=input&ttsspeed=1"
    whole = p1 + p2 + p3 + p4 +p45 + p5
    return whole

if __name__ == '__main__':
    app.run()
