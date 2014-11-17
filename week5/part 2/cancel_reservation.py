def cancel_reservation(database, username):
    cursor = database.cursor()

    cursor.execute('''DELETE FROM Reservations WHERE username = ?''',
                  (username,))

    database.commit()
