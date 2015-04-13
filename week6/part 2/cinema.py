from sqlalchemy import Session
from movie import Movie
from projection import Projection


class Cinema:

    HALL_DIMENSION = 10
    FREE_SEAT_SIGN = '.'
    TAKEN_SEAT_SIGN = 'X'

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
            movie = self.session.query(Movie).filter(
                Movie.id == movie_id).one()
            projections = movie.projections

            projections_string = "Projections for movie {}:\n".format(
                movie.name)
            for projection in projections:
                projections_string += "{}\n".format(
                    self.projection_date_string(projection))
        else:
            projections = self.session.query(Projection).filter(
                Projection.movie_id == movie_id).order_by(
                Projection.time).all()
            # can I filter backref or ?

            movie = self.session.query(Movie).filter(
                Movie.id == movie_id).one()

            projections_string = '''projections for movie {}
                                    on date {}:\n'''.format(movie.name, date)
            for projection in projections:
                projections_string += "{}\n".format(
                    self.projection_time_string(projection))

        return projections_string

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

    def make_reservation(self):
        username = self.get_username()
        if self.is_give_up(username):
            return

        tickets = self.get_tickets()
        if self.is_give_up(tickets):
            return

        print(self.show_movies)

        movie_id = self.get_movie_id()
        if self.is_give_up(movie_id):
            return

        print(self.show_movie_projections(movie_id))

        projection_id = self.get_projection_id()
        if self.is_give_up(projection_id):
            return

        seats = self.get_seats(tickets)
            pass

    def is_give_up(self, string):
        return string == 'give_up'

    def get_username(self):
        username = input("Step 1 (User): Choose name> ")
        return username

    def get_tickets(self):
        tickets = input("Step 1 (User): Choose number of tickets> ")
        return tickets

    def get_movie_id(self):
        movie_id = input("Step 2 (Movie): Choose a movie by id> ")
        if movie_id != 'give_up':
            return int(movie_id)
        else:
            return movie_id

    def get_projection_id(self):
        projection_id = input("Step 3 (Projection): Choose a projection> ")
        if projection_id != 'give_up':
            return int(projection_id)
        else:
            return projection_id

    def show_available_seats(self, projection_id):
        projection = self.session.query(Projection).filter(
            Projection.id == projection_id).one()
        reservations = projection.reservations

        output = '''Available seats (marked with a dot):
                    \n   1 2 3 4 5 6 7 8 9 10'''
        for row in range(1, self.HALL_DIMENSION + 1):
            row_string = ""
            for col in range(1, self.HALL_DIMENSION + 1):
                if self.is_taken_spot(reservations, row, col):
                    row_string = row_string + " " + self.TAKEN_SEAT_SIGN
                else:
                    row_string += " " + self.FREE_SEAT_SIGN
            if row == self.HALL_DIMENSION:
                output += "\n{}{}".format(row, row_string)
            else:
                output += "\n{} {}".format(row, row_string)

    def is_taken_spot(self, reservations, row, col):
        reserved = list(filter(lambda x: x.row == row and x.col == col,
                               reservations))
        return len(reserved) == 1

    def get_seats(self, tickets):
        pass
