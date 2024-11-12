#!/usr/bin/python3
if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])
    cursor = db.cursor()

    cursor.execute("Select * from states")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
