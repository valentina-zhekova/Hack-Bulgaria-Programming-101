def show_movies(database):
    cursor = database.cursor()

    movies = cursor.execute('''SELECT * FROM Movies ORDER BY rating''')
    print("Current movies:")
    for movie in movies:
        print("[{}] - {} ({})".format(movie['id'],
                                      movie['name'],
                                      movie['rating']))
