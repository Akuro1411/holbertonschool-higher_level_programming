#!/usr/bin/python3
"""MySQLdb and sys are imported"""


if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])
    cursor = db.cursor()
    query = "select c.id, c.name, s.name from cities c \
    join states s where c.state_id=s.id and binary s.name=%s order by c.id"

    cursor.execute(query, (argv[4], ))
    rows = cursor.fetchall()
    for index, row in enumerate(rows):
        if index != len(rows) - 1:
            print(row[1], end=", ")
        else:
            print(row[1])
    cursor.close()
    db.close()
