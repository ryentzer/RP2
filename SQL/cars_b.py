import sqlite3

with sqlite3.connect('cars.db') as conn:
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS inventory")

    cursor.execute(""" CREATE TABLE IF NOT EXISTS inventory
        (make TEXT, model TEXT, qty INT) """)

    cursor.execute(""" CREATE TABLE IF NOT EXISTS orders
        (make TEXT, model TEXT, order_date TEXT) """)

    cars = [
        ('Ford', 'Mustang', 15),
        ('Chevy', 'Chevelle', 1),
        ('Chevy', 'Nova', 2),
        ('Chevy', 'Camaro', 12),
        ('VW', 'Bug', 3),
        ('JEEP', 'Wrangler', 8),

    ]

    orders = [
        ('Ford', 'Mustang', '2014-04-03'),
        ('Ford', 'Mustang', '2014-02-05'),
        ('JEEP', 'Wrangler', '2013-12-03'),
        ('Chevy', 'Mustang', '2013-10-04'),
        ('Ford', 'Mustang', '2013-09-03'),
        ('JEEP', 'Wrangler', '2013-08-03'),
        ('Chevy', 'Mustang', '2014-04-23'),
        ('VW', 'Bug', '2013-06-03'),
        ('Chevy', 'Mustang', '2014-02-13'),
        ('Ford', 'Mustang', '2014-06-04'),
        ('Chevy', 'Mustang', '2013-04-03'),
        ('Chevy', 'Mustang', '2013-04-03'),
        ('Ford', 'Mustang', '2013-09-15'),
        ('JEEP', 'Wrangler', '2013-07-12'),
        ('Ford', 'Mustang', '2013-04-07'),
        ('VW', 'Bug', '2013-03-31'),
    ]

    cursor.executemany("""INSERT into inventory VALUES(?, ?, ?)""", cars)

    cursor.executemany("""INSERT into orders VALUES(?, ?, ?)""", orders)