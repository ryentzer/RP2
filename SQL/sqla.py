import sqlite3

with sqlite3.connect('new.db') as conn:

    c = conn.cursor()

    c.execute('''
        CREATE TABLE population
        (city TEXT, state TEXT, population INT)
        ''')
