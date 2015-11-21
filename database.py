import sqlite3

import fluently

file = open('frazy', 'rb')
for line in file:
    line = line.decode('UTF-8')
    if line.startswith('1'):
        category = line[1:]
        print(category)
    else:
        line = line.split(';')
        polish = line[0]
        english = line[1]
        print(polish)
        english = english.split('(')
        english = english[0]
        print(english)
        cur = sqlite3.connect('/Users/Marcin/PycharmProjects/fluently/database/fluently.db')
        cur.execute("""
    INSERT INTO phrases
    (priority, english, polish, category)
    VALUES (""" + str(0) + ', "' + english + '", "' + polish + '", "' + category + '" )')

        cur.commit()

