#!/usr/bin/python3
""" Module that lists all states from the database"""
import MySQLdb
import sys

def list_states_by_name(username, password, database):

    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        states = cursor.fetchall()
        for state in states:
            print(state[0])

    except Exception as err:
        print(f"Error connecting to database: {err}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    list_states_by_name("my_username", "my_password", "hbtn_0e_0_usa")
