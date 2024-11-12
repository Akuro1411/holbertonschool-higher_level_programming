#!/usr/bin/python3
"""MySQLdb and sys are imported"""


if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])
    cursor = db.cursor()

    cursor.execute("Select * from states where name like %s order by id", ('N%',))
    rows = cursor.fetchall()
    for row in rows:
        # it could be written with conditional statement too
        print(row)

    cursor.close()
    db.close()
