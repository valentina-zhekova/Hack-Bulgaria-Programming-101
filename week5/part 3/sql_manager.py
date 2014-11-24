import sqlite3
from Client import Client

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''CREATE TABLE IF NOT EXISTS
                      clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                              username TEXT,
                              password TEXT,
                              balance REAL DEFAULT 0,
                              message TEXT)'''

    cursor.execute(create_query)


def change_message(new_message, logged_user):
    update_sql = """UPDATE clients SET message = ? WHERE id = ?"""
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    update_sql = """UPDATE clients SET password = ? WHERE id = ?"""
    cursor.execute(update_sql, (new_pass, logged_user.get_id()))
    conn.commit()


def register(username, password):
    insert_sql = """INSERT INTO clients(username, password)
                    VALUES (?, ?)"""
    cursor.execute(insert_sql, (username, password))
    conn.commit()


def login(username, password):
    select_query = """SELECT id, username, balance, message
                      FROM clients WHERE username = ?
                      AND password = ? LIMIT 1"""

    cursor.execute(select_query, (username, password))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False

def is_password_strong(username, password):

    if len(password) < 8:
        return False
    else:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        password_chars = list(password)
        password_low_case = list(filter(lambda x: x in alphabet,
                                        password_chars))
        password_up_case = list(filter(lambda x: x in alphabet.upper(),
                                       password_chars))
        password_numbers = list(filter(lambda x: x in range(0, 9),
                                       password_chars))

        if
