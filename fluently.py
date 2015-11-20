import json
import sqlite3
from contextlib import closing
import os

from flask import Flask, render_template, request, g

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
    #tworzenie strony
    con = get_db().execute('select * from phrases')
    phrases = []
    for phrase in con:
        print(phrase)
        phrases.append(phrase)
    return render_template('index.html', phrases = phrases)


if __name__ == '__main__':
    app.run()