#!/usr/bin/python3

"""
    Script changes the name of a state object from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':
    import sys
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    name_update = session.query(State).get(2)
    name_update.name = "New Mexico"

    session.add(name_update)
    session.commit()
    session.close()
