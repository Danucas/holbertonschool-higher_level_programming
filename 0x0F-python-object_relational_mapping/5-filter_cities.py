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
                 WHERE
                      cities.state_id=(
                             SELECT
                                  states.id
                             FROM
                                  states
                             WHERE BINARY
                                  states.name=%(state)s)
                 ORDER BY
                      cities.id ASC""", {
                          'state': argument
                      })
    res = {city[0] for city in c.fetchall()}
    print(', '.join(res))

if __name__ == '__main__':
    main()
