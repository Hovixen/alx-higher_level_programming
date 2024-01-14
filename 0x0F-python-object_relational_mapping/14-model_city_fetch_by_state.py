#!/usr/bin/python3

"""
    Script prints all City object from the database hbtn_0e_14_usa
"""

if __name__ == '__main__':
    import sys
    from model_state import State
    from model_city import City, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City).order_by(City.id).all()

    for city in result:
        print('{}: ({}) {}'.format(city.state.name, city.id, city.name))

    session.close()
