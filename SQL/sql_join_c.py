import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()

    c.execute("""SELECT population.city, population.population,
      regions.region FROM population, regions WHERE
      population.city = regions.city""")

    rows = c.fetchall()
    for r in rows:
        print "{}'s population is {}. It's located in the {} region.".format(r[0], r[1], r[2])