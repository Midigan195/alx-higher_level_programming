#!/usr/bin/python3
"""
Script prints a list of all the cities from database
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
    cursor.execute("""
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
        """)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
