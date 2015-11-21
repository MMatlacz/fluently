import sqlite3

import fluently

file = open('frazy', 'rb')
for line in file:
    line = line.decode('UTF-8')
    line = line.split(';')
    print(line[0])
    print(line[1])
    print(line[2])
    cur = sqlite3.connect('/Users/Marcin/PycharmProjects/fluently/database/fluently.db')
    cur.execute("""
    INSERT INTO culture
    (country, text, image)
    VALUES (""" + str(line[0]) + ', "' + str(line[1]) + '", "' + str(line[2]) + ' )');

    cur.commit()