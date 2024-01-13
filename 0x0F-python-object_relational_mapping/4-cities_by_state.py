#!/usr/bin/python3

"""
    Script lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    if len(sys.argv) != 4:
        sys.exit(1)

    user, password, db = sys.argv[1:4]

    connX = MySQLdb.connect(host="localhost", port=3306, user=user,
                            passwd=password, db=db)
    cur= connX.cursor()

    sql_query = (
            "SELECT cities.id, cities.name, states.name "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id ASC;"
    )

    cur.execute(sql_query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    connX.close()
