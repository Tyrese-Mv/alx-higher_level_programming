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
    p1 = "SELECT cities.id, cities.name, states.name"
    p2 = "FROM cities INNER JOIN states ON cities.state_id=states.id"
    p3 = "ORDER BY cities.id ASC"
    query = "{} {} {};".format(p1, p2, p3)
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
