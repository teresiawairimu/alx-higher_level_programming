#!/usr/bin/python3
"""Lists all states with a name matching the argument from database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )
    cur = db.cursor()
    query = (
            "SELECT * FROM states WHERE name LIKE '{}'"
            "ORDER BY id ASC"
            ).format(sys.argv[4])
    cur.execute(query)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
