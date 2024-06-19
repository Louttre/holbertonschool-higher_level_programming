#!/usr/bin/python3
"""
Import the MySQLdb and sys module
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        post=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    query = ("SELECT * FROM cities ORDER "
             "BY cities.id ASC;")
    cursor.execute(query)
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
