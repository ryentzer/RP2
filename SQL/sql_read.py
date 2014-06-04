__author__ = 'ryentzer'

import sqlite3

with sqlite3.connect('employees.db') as connection:
    c = connection.cursor()
    c.execute("SELECT firstname, lastname FROM employees")

    rows = c.fetchall()

    for row in rows:
        print row[0] + " " + row[1] + " is cool."