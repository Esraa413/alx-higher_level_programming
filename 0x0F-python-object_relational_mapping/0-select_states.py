#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa
the module MySQLdb
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cu = db.cursor()
    cu.execute("SELECT * FROM states")
    rows = cu.fetchall()
    for row in rows:
        print(row)
    cu.close()
    db.close()
