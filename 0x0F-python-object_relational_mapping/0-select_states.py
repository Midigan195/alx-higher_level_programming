#!/usr/bin/python3
"""
Script prints a list of all the states from database
"""
import MySQLdb
import sys

if __name__ == "__main__":
    usr = sys.argv[1]
    pw = sys.argv[2]
    dab = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=usr,
                         passwd=pw,
                         db=dab)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
