#!/usr/bin/python3
"""Lists all states from database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MYSQLdb.connect(username=sys.argv[1], password=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(state for state in c.fetchall()]