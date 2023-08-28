#!/usr/bin/python3
'''script that lists all cities from the database hbtn_0e_4_usa'''
import MySQLdb
import sys


if __name__ == '__main__':
    db_connection = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3],
            port=3306)
    cursor = db_connection.cursor()
    cursor.execute(
            "SELECT cities.id, cities.name, states.name\
            FROM cities\
            INNER JOIN states\
            ON cities.state_id = states.id\
            ORDER BY cities.id")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db_connection.close()
