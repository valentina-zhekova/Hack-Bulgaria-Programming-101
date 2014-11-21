from connection import Base
from movie import Movie
from projection import Projection
from reservation import Reservation
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def main():
    engine = create_engine("sqlite:///cinema_database.db")
    Base.metadata.create_all(engine)
    session = Session(bind=engine)

    session.add_all([Movie(name="The Hunger Games: Catching Fire", rating=7.9),
                     Movie(name="Wreck-It Ralph", rating=7.8),
                     Movie(name="Her", rating=8.3)])

    session.add_all([Projection(movie_id=1, type="3D",
                                date="2014-04-01", time="19:10"),
                     Projection(movie_id=1, type="2D",
                                date="2014-04-01", time="19:00"),
                     Projection(movie_id=1, type="4DX",
                                date="2014-04-02", time="21:00"),
                     Projection(movie_id=3, type="2D",
                                date="2014-04-05", time="20:20"),
                     Projection(movie_id=2, type="3D",
                                date="2014-04-02", time="22:00"),
                     Projection(movie_id=2, type="2D",
                                date="2014-04-02", time="19:30")])

    session.add_all([Reservation(username="RadoRado", projection_id=1,
                                 row=2, col=1),
                     Reservation(username="RadoRado", projection_id=1,
                                 row=3, col=5),
                     Reservation(username="RadoRado", projection_id=1,
                                 row=7, col=8),
                     Reservation(username="Ivo", projection_id=3,
                                 row=1, col=1),
                     Reservation(username="Ivo", projection_id=3,
                                 row=1, col=2),
                     Reservation(username="Mysterious", projection_id=5,
                                 row=2, col=3),
                     Reservation(username="Mysterious", projection_id=5,
                                 row=2, col=4)])

    session.commit()

if __name__ == '__main__':
    main()
