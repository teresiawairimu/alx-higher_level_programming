#!/usr/bin/python3
"""Takes in the name of the state as argument
lists all cities of the states
from database hbtn_0e_0_usa
"""
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
    query = """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """
    cur.execute(query, (sys.argv[4],))
    cities = cur.fetchall()
    print(", ".join(city[0] for city in cities))
    cur.close()
    db.close()
