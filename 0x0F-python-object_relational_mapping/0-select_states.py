#!/usr/bin/python3

import MySQLdb
import sys


if __name__ == "__main__":
	db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
	m = db.cursor()
	m.execute("SELECT * FROM states")
	rows = m.fetchall()
	for row in rows:
		print(row)
	m.close()
	db.close()
