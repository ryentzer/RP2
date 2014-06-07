# sql.py - Use an SQLite3 db to create the table for our blog

import sqlite3

# create a new db if doesn't already exist
with sqlite3.connect('blog.db') as connection:
    c = connection.cursor()

    c.execute(""" CREATE TABLE IF NOT EXISTS posts
      (title TEXT, post TEXT) """ )

    # insert dummy data
    dummyData = [
        ('Good', 'I\'m good.'),
        ('Well', 'I\'m well.'),
        ('Excellent', 'I\'m excellent.'),
        ('Okay', 'I\'m okay.')
    ]

    c.executemany("INSERT INTO posts values(?, ?)",dummyData)