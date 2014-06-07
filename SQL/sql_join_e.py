import sqlite3

# output car's make and model on one line
# quantity on another
# order_dates on last line
with sqlite3.connect("cars.db") as conn:
    c = conn.cursor()

    c.execute("""SELECT inventory.model, inventory.make, inventory.qty, orders.order_date
    from inventory, orders WHERE inventory.make = orders.make ORDER BY order_date DESC""")

    rows = c.fetchall()

    for r in rows:
        print "{} {}".format(r[1], r[0])
        print "Quantity: " + str(r[2])
        print "Order Dates: " + r[3]
