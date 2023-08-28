#!/usr/bin/python3
'''takes in an argument and displays all values
in the states table of hbtn_0e_0_usa'''
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
            "SELECT id, name FROM states\
            WHERE name LIKE BINARY '{}'\
            ORDER By id".format(sys.argv[4]))
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db_connection.close()
