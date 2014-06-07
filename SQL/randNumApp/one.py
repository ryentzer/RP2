# Add 100 random integers, ranging from 0 to 10
# to a new database called "newnum.db"

import random
import sqlite3

with sqlite3.connect('newnum.db') as conn:
    c = conn.cursor()

    c.execute("CREATE TABLE nums (nums INT)")
    nums = []

    for num in range(1,100):
        ran = random.randint(1, 101)
        nums.append(ran)

   # print nums
