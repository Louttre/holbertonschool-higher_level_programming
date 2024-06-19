"""
Import the MySQLdb and sys module
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(username=sys.argv[1}, password=sys.argv[2],
            database=sys.argv[3], host="localhost")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
