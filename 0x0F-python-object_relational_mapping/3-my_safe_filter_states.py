#!/usr/bin/python3

"""
    Script takes an argument that displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument
"""

if __name__ == '__main__':
    import sys
    import MySQLdb


    if len(sys.argv) != 5:
        print("Usage: {} <user> <password> <database> <state>".format(sys.argv[0]))
        sys.exit(1)

    user, passwd, db, state = sys.argv[1:5]


    connX = MySQLdb.connect(host="localhost", port=3306, user=user,
                            passwd=passwd, db=db)

    cur = connX.cursor()

    sql_query = (
            "SELECT * "
            "FROM states "
            "WHERE name LIKE BINARY '{}' "
            "ORDER BY id ASC;"
    )

    cur.execute(sql_query, (state,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    connX.close()
