#!/usr/bin/python3
""" Module that lists all states from the database"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Gets credentials from command-line arg and connect to MySQL server
    """
    db == MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()

    c.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id""")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
