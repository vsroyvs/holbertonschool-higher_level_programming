#!/usr/bin/python3
'''Module to list all states from database hbtn_0e_0_usa'''
import MySQLdb
import sys


if __name__ == '__main__':
    
    db_connection = MySQLdb.connect(host='localhost', user=sys.argv[1], password=sys.argv[2], database=sys.argv[3], port=3306)
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db_connection.close()
