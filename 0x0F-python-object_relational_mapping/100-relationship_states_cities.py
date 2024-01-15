#!/usr/bin/python3

"""
    Script creates the state California with the city San Francisco from the
    database hbtn_0e_100_usa
"""

if __name__ == '__main__':
    import sys
    from relationship_state import State
    from relationship_city import City, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="California", cities=[City(name="San Francisco")])
    session.add(state)
    session.commit()
    session.close()
