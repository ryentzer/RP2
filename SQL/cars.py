import sqlite3

with sqlite3.connect('cars.db') as conn:
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE inventory
        (Make TEXT, Model TEXT, Year INT) """)