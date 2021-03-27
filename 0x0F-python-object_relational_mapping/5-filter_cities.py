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

    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON cities.state_id=states.id WHERE states.name='{}' ORDER BY name ASC".format(argv[4]))
    query_rows = cur.fetchall()
    list_data = []
    for row in query_rows:
        list_data.append(row[0])
    print(', '.join(list_data))

    db.close()
