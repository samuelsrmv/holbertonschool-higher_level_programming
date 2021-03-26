#!/usr/bin/python3
"""Exercise
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """COnect
    """
    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3], port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    db.close()
