import sqlite3
from client import Client
from hashing import *
from settings import DB_NAME

conn = sqlite3.connect(DB_NAME)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT)'''

    cursor.execute(create_query)


def change_message(new_message, logged_user):
    update_sql = '''UPDATE clients
    SET message = {}
    WHERE id = {}'''.format(new_message, logged_user.get_id())
    cursor.execute(update_sql)
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    update_sql = '''UPDATE clients
    SET password = {}
    WHERE id = {}'''.format(encode_pass(new_pass), logged_user.get_id())
    cursor.execute(update_sql)
    conn.commit()


def register(username, password):
    REGISTER_IN_SYSTEM = '''INSERT INTO clients(USERNAME, PASSWORD)
    VALUES(?, ?)
    '''
    cursor.execute(REGISTER_IN_SYSTEM, (username, encode_pass(password)))
    conn.commit()


def login(username, password):
    select_user = '''SELECT * FROM CLIENTS
    WHERE username = "{}"
    LIMIT 1
    '''.format(username)

    cursor.execute(select_user)
    user = cursor.fetchone()

    if(user['password'] == encode_pass(password)):
        return Client(user['id'], user['username'], user['balance'], user['message'])
    else:
        return False


def deposit(amount, logged_user):
    update_sql = '''UPDATE clients
    SET balance = balance + {}
    WHERE id = {}'''.format(amount, logged_user.get_id())
    cursor.execute(update_sql)
    conn.commit()


def get_balance(logged_user):
    get_balance = '''SELECT * FROM CLIENTS
    WHERE id = {}
    LIMIT 1
    '''.format(logged_user.get_id())
    cursor.execute(get_balance)
    user = cursor.fetchone()

    return user['balance']

def withdraw(amount, logged_user):
    select_user = '''SELECT * FROM CLIENTS
    WHERE username = "{}"
    LIMIT 1
    '''.format(logged_user['username'])
    cursor.execute(select_user)
    user = cursor.fetchone()

    if user['balance'] > amount:
        update_sql = '''UPDATE clients
        SET balance = balance - {}
        WHERE id = {}'''.format(amount, logged_user.get_id())
        cursor.execute(update_sql)
        conn.commit()
        return True
    else:
        return False
