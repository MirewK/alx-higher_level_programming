#!/usr/bin/python3
""" Module that lists all states from the database"""
import MySQLdb
import sys

if __name__ == "__main__":
    #Gets credentials from command-line arg and connect to MySQL server
    db == MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    cursor.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in cursor.fetchall() if state[1][0] == "N"]
