#!/usr/bin/python3
"""
Import the MySQLdb and sys module
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name"
                   " LIKE BINARY %s ORDER "
                   "BY state.id ASC;", (sys.argv[4],))
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
