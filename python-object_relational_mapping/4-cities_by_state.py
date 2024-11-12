#!/usr/bin/python3
"""MySQLdb and sys are imported"""


if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])
    cursor = db.cursor()
    query = "select c.id, c.name, s.name from cities c \
    join states s where c.state_id=s.id"

    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
