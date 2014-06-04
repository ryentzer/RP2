import sqlite3

with sqlite3.connect('employees.db') as connection:
    c = connection.cursor()
    # delete
    c.execute("DELETE FROM employees WHERE lastname='Yentzer'")

    #create
    c.execute("INSERT INTO employees VALUES ('Rick', 'Yetzner')")

    #update
    c.execute("UPDATE employees SET lastname = 'Yentzer' WHERE lastname='Yetzner'")

    #read
    c.execute("SELECT lastname FROM employees WHERE lastname='Yentzer'")

    rows = c.fetchall()

    for r in rows:
        print r[0]