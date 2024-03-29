#!/usr/bin/python3

"""
    Script prints the first State object from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':
    import sys
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()

    if state:
        print('{}: {}'.format(state.id, state.name))
    else:
        print('Nothing')
    session.close()
