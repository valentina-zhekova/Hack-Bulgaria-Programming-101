HALL_DIMENSION = 10


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
