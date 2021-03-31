#!/usr/bin/python3
"""Exercise
"""
import MySQLdb
from sys import argv


def filter():
    """function filter
    """
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC"
                .format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == argv[4]:
            print(row)

    db.close()

if __name__ == '__main__':
    filter()
