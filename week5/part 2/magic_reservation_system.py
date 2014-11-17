# to fix -> finalize writes data not before that
#        -> give_up; cancel_reservation; help yet to be done
#        -> refactor & some modules; it's some very ugly file right now
import sqlite3

DATABASE_FILE = "cinema_database"
HALL_DIMENSION = 10
TAKEN_SEAT_SIGN = "X"
FREE_SEAT_SIGN = "."


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

    cursor.execute('''SELECT name FROM Movies WHERE id = ?''', (movie_id,))
    movie = cursor.fetchone()

    if date is None:
        cursor.execute('''SELECT id, type, date, time
                          FROM Projections
                          WHERE movie_id = ?
                          ORDER BY date''', (movie_id,))
    else:
        cursor.execute('''SELECT id, type, time
                          FROM Projections
                          WHERE movie_id = ? AND date = ?
                          ORDER BY time''', (movie_id, date))
    projections = cursor.fetchall()

    if date is None:
        prompt_string = 'Projections for movie "{}":'
        print(prompt_string.format(movie['name']))
        for projection in projections:
            available_seats = count_available_seats(database, projection['id'])
            output_string = '[{}] - {} {} ({}) - {} spots available'
            print(output_string.format(projection['id'], projection['date'],
                                       projection['time'], projection['type'],
                                       available_seats))
    else:
        prompt_string = 'Projections for movie "{}" on date {}:'
        print(prompt_string.format(movie['name'], date))
        for projection in projections:
            available_seats = count_available_seats(database, projection['id'])
            output_string = '[{}] - {} ({}) - {} spots available'
            print(output_string.format(projection['id'], projection['time'],
                                       projection['type'], available_seats))


def count_available_seats(database, projection_id):
    cursor = database.cursor()

    cursor.execute('''SELECT count(*) FROM Reservations
                      WHERE projection_id = ?''', (projection_id,))
    reservations_count = cursor.fetchone()

    available_seats = HALL_DIMENSION ** 2 - reservations_count[0]
    return available_seats


def make_reservation(database):
    username = input("Step 1 (User): Choose name> ")
    tickets = input("Step 1 (User): Choose number of tickets> ")

    show_movies(database)
    movie = input("Step 2 (Movie): Choose a movie> ")

    show_movie_projections(database, movie)
    while True:
        projection = input("Step 3 (Projection): Choose a projection> ")
        if tickets > count_available_seats(database, projection):
            print("There are not enough free spots, try another projection!")
        else:
            break

    available_spots(database, projection)

    reserved_seats = []
    cursor = database.cursor()

    for ticket in range(1, tickets + 1):
        while True:
            prompt = "Step 4 (Seats): Choose seat {}> ".format(ticket)
            seat = input(prompt)[1:-1].split(", ")
            row = seat[0]
            col = seat[1]

            row_out_of_bounds = row < 1 or row > HALL_DIMENSION
            col_out_of_bounds = col < 1 or col > HALL_DIMENSION
            if row_out_of_bounds or col_out_of_bounds:
                print("Lol...NO!")
            elif is_taken_spot(database, projection, row, col):
                print("This seat is already taken!")
            else:
                cursor.execute('''INSERT INTO Reservations(username,
                                                           projection_id,
                                                           row, col)
                                  VALUES(?,?,?,?)''', (username, projection,
                                                       row, col))

                reserved_seats.append((row, col))

                break

    ordered_reservations = sorted(reserved_seats)
    cursor.execute('''SELECT name, rating FROM Movies WHERE id =?''', (movie,))
    the_movie = cursor.fetchone()
    movie_string = '{} ({})'.format(the_movie['name'], the_movie['rating'])
    cursor.execute('''SELECT date, time, type FROM Projections WHERE id = ?''',
                  (projection,))
    proj = cursor.fetchone()
    projection_string = "{} {} ({})".format(proj['date'],
                                            proj['time'],
                                            proj['type'])

    output_string = '''This is your reservation:
                       \nMovie: {}\nDate and Time: {}\nSeats {}'''

    print(output_string.format(movie_string,
                               projection_string,
                               ordered_reservations))

    is_final = input("Step 5 (Confirm - type 'finalize') > ")
    if is_final == 'finalize':
        print("Thanks")


def available_spots(database, projection_id):
    print("Available seats (marked with a dot):"
          "\n   1 2 3 4 5 6 7 8 9 10")
    for row in range(1, HALL_DIMENSION + 1):
        print("{} ".format(row))
        for col in range(1, HALL_DIMENSION + 1):
            if is_taken_spot(database, projection_id, row, col):
                print(TAKEN_SEAT_SIGN)
            else:
                print(FREE_SEAT_SIGN)


def is_taken_spot(database, projection_id, row, col):
    cursor = database.cursor()

    cursor.execute('''SELECT row, col FROM Reservations
                      WHERE projection_id = ?''', (projection_id,))
    taken_spots = cursor.fetchall()

    for spot in taken_spots:
        if spot['row'] == row and spot['col'] == col:
            return True
    return False


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
        user_choice = input("\ncommand> ")

        command = user_choice.split()[0]
        arguments = user_choice.split()[1:]

        if command == 'exit':
            break
        elif command == 'show_movies':
            show_movies(database)
        elif command == 'make_reservation':
            make_reservation(database)
        elif command == 'show_movie_projections':
            if len(arguments) == 2:
                show_movie_projections(database, arguments[0], arguments[1])
            else:
                show_movie_projections(database, arguments[0])
        else:
            print("There is no such command, try again!")

    database.close()


def main():
    interface()

if __name__ == '__main__':
    main()
