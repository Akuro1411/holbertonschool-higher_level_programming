#!/usr/bin/python3
"""MySQLdb and sys are imported"""


if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])
    cursor = db.cursor()
    query = "Select * from states where binary name='{name}' order by id"

    cursor.execute(query.format(name=argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
