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
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
    cursor.execute(query. format(st_name))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
