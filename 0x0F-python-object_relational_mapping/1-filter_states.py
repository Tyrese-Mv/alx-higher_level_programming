#!/usr/bin/python3
"""select states"""
import MySQLdb
import sys


if __name__ == "__main__":
    username, password, db_name = sys.argv[1:4]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
        )
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC;"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
