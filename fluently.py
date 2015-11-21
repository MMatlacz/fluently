import json
import sqlite3
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


def write_most_popular_places(localization):
    print("dsaa")
    # baza.write("localization ++")


if __name__ == '__main__':
    app.run()

    # connect_db().execute( "update phrases set english = 'hello', polish = 'czesc', category = 'basic' where id = 0" );
