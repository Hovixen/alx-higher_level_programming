#!/usr/bin/python3

"""
    Script takes in the name of a state as an argument and lists all
    cities of a state, using the database hbtn_0e_4_usa
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    if len(sys.argv) != 5:
        sys.exit(1)
    
    user, password, db, states = sys.argv[1:5]

    connX = MySQLdb.connect(host="localhost", port=3306, user=user,
                            passwd=password, db=db)
    cur = connX.cursor()

    sql_query = (
            "SELECT cities.name "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "WHERE states.name LIKE BINARY %s "
            "ORDER BY cities.id ASC;"
    )

    cur.execute(sql_query, (states,))

    rows = cur.fetchall()

    for i, row in enumerate(rows):
        if i > 0:
            print(', ', end='')
        print(row[0], end='')
    print()

    cur.close()
    connX.close()
