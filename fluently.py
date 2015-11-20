import sqlite3

from flask import Flask, render_template, g

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
    cur = get_db().execute('select * from phrases')
    for phrase in cur:
        print(phrase)
        phrases = []
        phrases.append(phrase)
    print(phrases)
    return render_template('index.html', phrases = phrases)



@app.route('/countPhrase', methods=['POST'])
def get_count_phrase():
    return connect_db().execute('select priority from phrases where id is 0')

def write_most_popular_places( localization ):
    print("dsaa")
    #baza.write("localization ++")


def increment_phrase( phrase_id ):
    connect_db().execute('update phrases set priority = priority + 1 where id is %id') %phrase_id

if __name__ == '__main__':
    app.run()

    #connect_db().execute( "update phrases set english = 'hello', polish = 'czesc', category = 'basic' where id = 0" );