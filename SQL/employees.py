import csv
import sqlite3

with sqlite3.connect('employees.db') as connection:
    c = connection.cursor()

    try:
        c.execute('CREATE TABLE employees(firstname, lastname)')

        # open csv file and assign to variable
        employees = csv.reader(open('employees.csv', 'rU'))

        c.executemany('INSERT INTO employees VALUES (?,?)', employees)

    except sqlite3.OperationalError:
        print "Oops! Something went wrong. Try again."