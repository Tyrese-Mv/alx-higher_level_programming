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
    p1 = "SELECT cities.name"
    p2 = "FROM cities JOIN states ON cities.state_id=states.id"
    p21 = "WHERE states.name = %s"
    p3 = "ORDER BY cities.id ASC"
    query = "{} {} {} {};".format(p1, p2, p21, p3)
    cursor.execute(query, (state,))
    rows = cursor.fetchall()
    strBuilder = ""
    for row in rows:
        strBuilder += row[0] + ", "
    print(strBuilder[0:-2:])
    cursor.close()
    db.close()
