import requests
import sqlite3
import hashlib
import datetime
from Client import Client

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT)'''

    cursor.execute(create_query)


def create_bruteforce_protection():
    create_query = '''create table if not exists protection(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user TEXT REFERENCES clients(username),
                    tries INTEGER DEFAULT 0,
                    first_try TEXT DEFAULT "1990-01-31 00:00:00.0")'''
    cursor.execute(create_query)
    # all_users = cursor.execute('''SELECT username FROM clients''').fetchall()
    # for user in all_users:
    #     cursor.execute('''INSERT INTO protection (user) VALUES(?)''', (user))
    # conn.commit()


def start_protection():
    create_bruteforce_protection()
    # all_users = cursor.execute('''SELECT username FROM clients''').fetchall()
    # for user in all_users:
    #     cursor.execute('''INSERT INTO protection (user) VALUES(?)''', (user))
    # conn.commit()


def update_protection(username):
    available_users = cursor.execute("SELECT user FROM protection").fetchall()
    current_time = datetime.datetime.now()
    if (username,) in available_users:
        cursor.execute('''UPDATE protection SET tries = tries + 1 WHERE user = ?''', (username,))
        failed_try = cursor.execute(
            '''SELECT tries FROM protection WHERE user = ?''', (username,)).fetchone()
        print(failed_try[0] % 5)
        if failed_try[0] % 5 == 0:
            cursor.execute(
                '''UPDATE protection SET first_try = ?, tries = 0 WHERE user = ?''', (current_time, username))
            print("You are dumb!")
    conn.commit()


def cooldown(username):
    current_time = datetime.datetime.now()
    # first_try_empty = cursor.execute("SELECT first_try FROM protection WHERE user = (?)", (username,)).fetchone()
    # if first_try_empty[0] == 0:
        # more than 5, which prevents the user from logging for a period of time.
        # return 99999
    bantime_raw = cursor.execute("SELECT first_try FROM protection WHERE user = (?)", (username,)).fetchone()
    bantime = datetime.datetime.strptime(bantime_raw[0], "%Y-%m-%d %H:%M:%S.%f")
    diff = current_time - bantime
    diff_minutes = diff.total_seconds() / 60
    # if diff_minutes > 5.0:
    #     cursor.execute("UPDATE protection SET tries = 0 WHERE user = (?)", (username,))
    return diff_minutes


    # first_try = cursor.execute(
    #     '''SELECT first_try FROM protection WHERE user = username''')
    # cursor.execute(
    #     '''INSERT INTO protection (user, tries) VALUES(?,?)''', (username, current_tries))
    # if current_tries > 5 and datetime.datetime.now() - first_try < 5:
    #     print("You should wait {} minutes before trying to log in again".format(
    #         datetime.datetime.now() - first_try


def change_message(new_message, logged_user):
    cursor.execute("UPDATE clients SET message = (?) WHERE id = (?)", (
        new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    new_pass
    cursor.execute("UPDATE clients SET password = (?) WHERE id = (?)", (
        hashlib.sha1(new_pass.encode("UTF-8")).hexdigest(), logged_user.get_id()))
    conn.commit()


def register(username, password):
    cursor.execute("INSERT into clients(username, password) VALUES (?,?)", (
        username, hashlib.sha1(password.encode("UTF-8")).hexdigest()))
    cursor.execute("INSERT into protection(user) VALUES(?)", (username,))
    conn.commit()


def login(username, password):
    cursor.execute("SELECT id, username, balance, message FROM clients WHERE username = (?) AND password = (?) LIMIT 1",  (
        username, hashlib.sha1(password.encode("UTF-8")).hexdigest()))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False
