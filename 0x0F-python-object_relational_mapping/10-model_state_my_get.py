#!/usr/bin/python3

"""
    Script prints the state object with the name passed as an argument
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

    state = session.query(State).filter(State.name == sys.argv[4]).first()

    if state:
        print('{}'.format(state.id))
    else:
        print('Not found')

    session.close()
