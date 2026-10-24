#!/usr/bin/python3
"""Safely displays states in hbtn_0e_0_usa whose name matches the argument."""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s "
                "ORDER BY id ASC", (sys.argv[4],))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
