#!/usr/bin/python3
""" Module that lists all states from the database"""
import MySQLdb
import sys

if __ name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, 
            user=username, passwd=password, db=database)
        c = db.cursor()
        c.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
        states = c.fetchall()
        for state in states:
            print(state)
        c.close()
        db.close()
