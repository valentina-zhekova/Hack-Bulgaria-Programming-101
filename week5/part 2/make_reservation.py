# the function turned out pretty messed up
# and give_up option isn't accurate
from show_movies import show_movies
from show_movie_projections import *

HALL_DIMENSION = 10
TAKEN_SEAT_SIGN = "X"
FREE_SEAT_SIGN = "."
GIVE_UP = 0


def make_reservation(database):
    username = input("Step 1 (User): Choose name> ")
    if is_giving_up(username):
        return
    tickets = input("Step 1 (User): Choose number of tickets> ")
    if is_giving_up(tickets):
        return
    else:
        tickets = int(tickets)

    show_movies(database)
    movie_id = input("Step 2 (Movie): Choose a movie> ")
    if is_giving_up(movie_id):
        return

    show_movie_projections(database, movie_id)
    projection_id = choose_projection(database, tickets)
    if projection_id == GIVE_UP:
        return

    available_spots(database, projection_id)

    chosen_seats = choose_seats(database, projection_id, tickets)
    if choose_seats == GIVE_UP:
        return

    reservation_info(database, movie_id, projection_id, sorted(chosen_seats))

    finalize(database, username, projection_id, chosen_seats)
    if finalize == GIVE_UP:
        return


def is_giving_up(check_string):
    return check_string == 'give_up'


def choose_projection(database, tickets):
    while True:
        projection_id = input("Step 3 (Projection): Choose a projection> ")
        if is_giving_up(projection_id):
            return GIVE_UP
        if tickets > count_available_seats(database, projection_id):
            print("There are not enough free spots, try another projection!")
        else:
            break
    return projection_id


def available_spots(database, projection_id):
    print("Available seats (marked with a dot):"
          "\n   1 2 3 4 5 6 7 8 9 10")
    for row in range(1, HALL_DIMENSION + 1):
        row_string = ""
        for col in range(1, HALL_DIMENSION + 1):
            if is_taken_spot(database, projection_id, row, col):
                row_string = row_string + " " + TAKEN_SEAT_SIGN
            else:
                row_string += " " + FREE_SEAT_SIGN
        if row == HALL_DIMENSION:
            print("{}{}".format(row, row_string))
        else:
            print("{} {}".format(row, row_string))


def is_taken_spot(database, projection_id, row, col):
    cursor = database.cursor()

    cursor.execute('''SELECT row, col FROM Reservations
                      WHERE projection_id = ?''', (projection_id,))
    taken_spots = cursor.fetchall()

    for spot in taken_spots:
        if spot['row'] == row and spot['col'] == col:
            return True
    return False


def choose_seats(database, projection_id, tickets):
    reserved_seats = []

    for ticket in range(1, tickets + 1):
        while True:
            prompt = "Step 4 (Seats): Choose seat {}> ".format(ticket)
            seat = input(prompt)
            if is_giving_up(seat):
                return GIVE_UP
            else:
                seat = seat[1:-1].split(", ")
                row = int(seat[0])
                col = int(seat[1])

            row_out_of_bounds = row < 1 or row > HALL_DIMENSION
            col_out_of_bounds = col < 1 or col > HALL_DIMENSION
            if row_out_of_bounds or col_out_of_bounds:
                print("Lol...NO!")
            elif is_taken_spot(database, projection_id, row, col):
                print("This seat is already taken!")
            else:
                reserved_seats.append((row, col))
                break
    return reserved_seats


def reservation_info(database, movie_id, projection_id, chosen_seats):
    cursor = database.cursor()

    cursor.execute('''SELECT name, rating FROM Movies WHERE id =?''',
                  (movie_id,))
    movie = cursor.fetchone()
    movie_string = '{} ({})'.format(movie['name'], movie['rating'])

    cursor.execute('''SELECT date, time, type FROM Projections WHERE id = ?''',
                  (projection_id,))
    projection = cursor.fetchone()
    projection_string = "{} {} ({})".format(projection['date'],
                                            projection['time'],
                                            projection['type'])

    output_string = '''This is your reservation:
                       \nMovie: {}\nDate and Time: {}\nSeats {}'''

    print(output_string.format(movie_string,
                               projection_string,
                               chosen_seats))


def finalize(database, username, projection_id, chosen_seats):
    while True:
        is_final = input("Step 5 (Confirm - type 'finalize') > ")
        if is_giving_up(is_final):
            return GIVE_UP
        elif is_final == 'finalize':
            break

    cursor = database.cursor()
    for seat in chosen_seats:
        row = seat[0]
        col = seat[1]
        table = "Reservations(username, projection_id, row, col)"
        cursor.execute('''INSERT INTO {} VALUES(?,?,?,?)'''.format(table),
                      (username, projection_id, row, col))

    database.commit()

    print("Thanks")
    return True
