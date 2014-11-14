import sqlite3

DATABASE_FILE = "cinema_database"


def show_movies(database):
    cursor = database.cursor()

    movies = cursor.execute('''SELECT * FROM Movies ORDER BY rating''')
    print("Current movies:")
    for movie in movies:
        print("[{}] - {} ({})".format(movie['id'],
                                      movie['name'],
                                      movie['rating']))


def show_movie_projections(database, movie_id, date=None):
    cursor = database.cursor()

    movie = cursor.execute('''SELECT name FROM Movies WHERE id = ?''',
                          (movie_id,))
    projections = cursor.execute('''SELECT id, type, date, time
                                    FROM Projections
                                    WHERE movie_id = ?
                                    ORDER BY date''', (movie_id,))

    print('Projections for movie {}:'.format(movie['name']))
    for projection in projections:
        print('[{}] - ')


def make_reservation(database):
    pass


def interface():

    print("You now have access to the cinema database,"
          "\nuse one of the following commands:"
          "\n\nshow_movies -> to see all movies ordered by rating"
          "\nshow_movie_projections <movie_id> [<date>] -> ..."
          "\nmake_reservation -> to get some seats"
          "\nexit -> to escape from here")

    database = sqlite3.connect(DATABASE_FILE)
    database.row_factory = sqlite3.Row

    while True:
        user_command = input("\ncommand> ")

        if user_command == 'exit':
            break
        elif user_command == 'show_movies':
            show_movies(database)
        elif user_command == 'make_reservation':
            make_reservation(database)
        elif user_command.split()[0] == 'show_movie_projections':
            parameters = user_command.split()[1:]
            show_movie_projections(database, parameters[0], parameters[1])
        else:
            print("There is no such command, try again!")

    database.close()


def main():
    interface()

if __name__ == '__main__':
    main()
