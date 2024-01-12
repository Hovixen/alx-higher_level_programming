#!/usr/bin/python3

"""
    Script lists all states with name starting with N from database
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    connX = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                            passwd=sys.argv[2], db=sys.argv[3])

    cur = connX.cursor()

    sql_query = (
            "SELECT * "
            "FROM states "
            "WHERE name LIKE BINARY 'N%' "
            "ORDER BY id ASC;"
    )

    cur.execute(sql_query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    connX.close()
