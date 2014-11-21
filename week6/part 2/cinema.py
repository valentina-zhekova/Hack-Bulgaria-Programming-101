from sqlalchemy import Session
from movie import Movie
from projection import Projection


class Cinema:

    def __init__(self, engine):
        self.session = Session(bind=engine)

    def show_movies(self):
        movies = self.session.query(Movie).order_by(Movie.rating).all()
        movies_string = "Current movies:\n"
        for movie in movies:
            movies_string += "{}\n".format(movie.__str__())
        return movies_string

    def show_movie_projections(self, movie_id, date=None):
        if date is None:
            projections = self.session.query(Projection).filter(
                Projection.movie_id == movie_id).order_by(
                Projection.date).all()

                movie.projections !!!!!!!!!!!!!!!!!!!!!!

            projections_string = "Projections for movie {}:\n".format()
            for projection in projections:
        else:
            projections = self.session.query(Projection).filter(
                Projection.movie_id == movie_id).order_by(
                Projection.time).all()
        return projections

    def available_spots(self, projection):
        taken_seats = len(projection.reservations)  # backref
        return 10 ** 2 - taken_seats

    def projection_date_string(self, projection):
        available_seats = self.available_spots(projection)
        return "[{}] - {} {} ({}) - {} spots available".format(projection.id,
                                                               projection.date,
                                                               projection.time,
                                                               projection.type,
                                                               available_seats)

    def projection_time_string(self, projection):
        available_seats = self.available_spots(projection)
        return "[{}] - {} ({}) - {} spots available".format(projection.id,
                                                            projection.time,
                                                            projection.type,
                                                            available_seats)
