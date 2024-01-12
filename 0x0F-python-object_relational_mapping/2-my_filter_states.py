#!/usr/bin/python3

"""
    Script takes an argument that displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument
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
            "WHERE name LIKE BINARY '{}' "
            "ORDER BY id ASC;".format(sys.argv[4])
    )

    cur.execute(sql_query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    connX.close()
