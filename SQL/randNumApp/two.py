# Prompt the user whether he or she would like to perform an aggregation
# (AVG, MAX, MIN, or SUM) or exit the program altogether.
import sqlite3

print "Random number aggregation game!"
print "I have a list of 100 random numbers."

def getUserChoice(answer):
    # print answer
    if answer == 'average':
        choice = 'AVG'
    elif answer == 'maximum':
        choice = 'MAX'
    elif answer == 'minimum':
        choice = 'MIN'
    elif answer == 'sum':
        choice = 'SUM'
    else:
        print "I didn't understand. Goodbye."

    return choice

answer = raw_input("Would you like to find the average, maximum, minimum or sum of the numbers? ")

getUserChoice(answer)

def performUserChoice(choice):
    with sqlite3.connect('newnum.db') as connection:
        c = connection.cursor()
        c.execute("SELECT * FROM nums")