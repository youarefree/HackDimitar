import sqlite3
from settings.sql_creation_settings import *
# from settings.general_settings import path
from hashing import *

# db = sqlite3.connect("/home/dimitar/101/Week10/cinema-Reservation/user_interface/cinema.db")
# db.row_factory = sqlite3.Row
# c = db.cursor()

GET_FREE_SEATS_MATRIX = '''SELECT * FROM RESERVATION
WHERE projection_id = {}
'''

LIST_ALL_MOVIES = '''SELECT * FROM movie ORDER BY RATING ASC
'''
GET_MOVIE_PROJECTIONS = '''SELECT * FROM PROJECTION
JOIN MOVIE ON PROJECTION.MOVIE_ID = MOVIE.ID
WHERE MOVIE.ID = {}
ORDER BY PROJECTION.PR_DATE ASC
'''

SELECT_USERS = '''SELECT * FROM USER
'''


LOG_USER = '''INSERT INTO log(user_id, logged_in)
VALUES(?, ?)
'''

SELECT_LOGGED_USERS = ''' SELECT * FROM LOG
'''
VKARAM_VIKITO = '''INSERT INTO user(username, password)
values(?, ?)
'''


# class CreateDB:
#     def __init__(self):
#         self.database = sqlite3.connect(path)
# #         self.cursor = self.database.cursor()

#     def drop_tables(self):
#         self.cursor.execute(DROP_USER_TABLE)
# #         self.cursor.execute(DROP_MOVIE_TABLE)
# #         self.cursor.execute(DROP_RESERVATION_TABLE)
# #         self.cursor.execute(DROP_PROJECTION_TABLE)
#         self.database.commit()

#     def create_tables(self):
#         self.cursor.execute(CREATE_USER_TABLE)
# #         self.cursor.execute(CREATE_MOVIE_TABLE)
# #         self.cursor.execute(CREATE_RESERVATION_TABLE)
# #         self.cursor.execute(CREATE_PROJECTION_TABLE)
#         self.database.commit()

#     def insert_into_tables(self):
# #        self.cursor.executemany(INSERT_MOVIE, movies)
#         self.cursor.executemany(INSERT_USER, users)
# #         self.cursor.executemany(INSERT_PROJECTION, projections)
# #         self.cursor.executemany(INSERT_RESERVATION, reservations)
#         self.database.commit()


def main():
    pass


if __name__ == "__main__":
    main()
