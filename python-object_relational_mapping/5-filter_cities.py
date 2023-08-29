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
            "SELECT cities.name\
            FROM cities\
            INNER JOIN states\
            ON cities.state_id = states.id\
            WHERE states.name = %s\
            ORDER BY cities.id", (sys.argv[4], ))
    esp = ""
    for row in cursor.fetchall():
        print(f"{esp}{row[0]}", end="")
        esp = ", "
    print()
    cursor.close()
    db_connection.close()
