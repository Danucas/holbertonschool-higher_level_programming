#!/usr/bin/python3
"""
Select the mysql table states by name starting with N
"""

import MySQLdb
import sys


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    argument = sys.argv[4]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         db=database,
                         user=username,
                         passwd=password)
    c = db.cursor()
    c.execute("""SELECT
                      cities.name
                 FROM
                      cities, states
                 WHERE BINARY
                      states.name = %s AND
                      cities.state_id = states.id
                 ORDER BY
                      cities.id ASC""", (argument,))
    print(', '.join(city[0] for city in c.fetchall()))

if __name__ == '__main__':
    main()
