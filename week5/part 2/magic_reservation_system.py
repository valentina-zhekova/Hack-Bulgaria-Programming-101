# maybe it needs some tests... and more
# modules - constants
from show_movies import show_movies
from show_movie_projections import show_movie_projections
from make_reservation import make_reservation
from cancel_reservation import cancel_reservation
import sqlite3

DATABASE_FILE = "cinema_database"
HALL_DIMENSION = 10


def help():
    print("\nYou can use one of the following commands:"
          "\n\nshow_movies -> to see all movies ordered by rating"
          "\nshow_movie_projections <movie_id> [<date>] -> "
          "order projections by time or if date is omitted by date"
          "\nmake_reservation -> to get some seats"
          "\ncancel_reservation <name> -> delete the person's reservations"
          "\nexit -> to escape from here")


def interface():

    print("You now have access to the cinema database,"
          "\ntype 'help' to see available options!")

    database = sqlite3.connect(DATABASE_FILE)
    database.row_factory = sqlite3.Row

    while True:
        user_choice = input("\ncommand> ")

        command = user_choice.split()[0]
        arguments = user_choice.split()[1:]

        if command == 'exit':
            break
        elif command == 'help':
            help()
        elif command == 'show_movies':
            show_movies(database)
        elif command == 'make_reservation':
            make_reservation(database)
        elif command == 'show_movie_projections':
            if len(arguments) == 2:
                show_movie_projections(database, arguments[0], arguments[1])
            else:
                show_movie_projections(database, arguments[0])
        elif command == 'cancel_reservation':
                cancel_reservation(database, arguments[0])
        else:
            print("There is no such command, try again!")

    database.close()


def main():
    interface()

if __name__ == '__main__':
    main()
