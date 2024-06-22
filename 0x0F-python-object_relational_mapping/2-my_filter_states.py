#!/usr/bin/python3
"""select states"""
import MySQLdb
import sys


if __name__ == "__main__":
    username, password, db_name, state = sys.argv[1:5]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
        )
    cursor = db.cursor()
    p1 = "SELECT * FROM"
    p2 = "ORDER BY states.id ASC"
    query = "{} states WHERE name = '{}' {};".format(p1, state, p2)
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
