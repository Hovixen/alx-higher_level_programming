#!/usr/bin/python3

"""
    Script lists all states from database hbtn_0e_0_usa
    in ascending order
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    connX = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")

    cur = connX.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()

    ## results = [tuple(rows) for row in rows]

    for row in rows:
        print(row)
    cur.close()
    connX.close()
