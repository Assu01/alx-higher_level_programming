#!/usr/bin/python3
""" takes name of a state as an argument and lists all cities"""
import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        host="localhost",
        port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities \
                    INNER JOIN states ON \
                    cities.state_id=states.id \
                    WHERE states.name=%s", (sys.argv[4],))
    row = cursor.fetchall()
    sp = ""
    ar = list(r[0] for r in row)
    for i in row:
        sp = sp + i[0] + ", "
    print(sp[0: -2:])
    cursor.close()
    db.close()
