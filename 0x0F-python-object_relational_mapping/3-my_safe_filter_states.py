#!/usr/bin/python3
"""
Script prints a list of all the states from database
that match user input
"""
import MySQLdb
import sys

if __name__ == "__main__":
    usr = sys.argv[1]
    pw = sys.argv[2]
    dab = sys.argv[3]
    st_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=usr,
                         passwd=pw,
                         db=dab)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        if row[1] == st_name:
            print(row)

    cursor.close()
    db.close()
