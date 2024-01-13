#!/usr/bin/python3

"""
    Script lists all state object that contain the letter 'a'
    from the database hbtn_0e_0_usa
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

    query = session.query(State)
    states = query.filter(State.name.like('%a%')).order_by(State.id).all()

    for state in states:
        print('{}: {}'.format(state.id, state.name))

    session.close()
