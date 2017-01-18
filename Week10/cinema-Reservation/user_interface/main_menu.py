import os
import getpass
from hashing import *
from settings.general_settings import path
from queries.manage_q import *
from queries.create_q import *
import sqlite3
import time


class mainMenu():

    def __init__(self, name):
        self.db = sqlite3.connect(path)
        self.db.row_factory = sqlite3.Row
        self.c = self.db.cursor()
        self.name_of_cinema = name

    # def welcome_screen(self)
    #     os.system('clear')
    #     print ('''Welcome to {}!
    #             You have the following options:
    #             1. To log into the hospital's system
    #             2. Register
    #             3. Get help
    #             4. Exit
    #             '''.format(self.name))
    #     choice = int(input("Input your choice: "))
    #     if choice == 1:
    #         self.log_into()
    #     elif choice == 2:
    #         self.register()
    #     elif choice == 3:
    #         self.help()
    #     elif choice == 4:
    #         self.exit()
    #     else:
    #         os.system('clear')
    #         print("No such option. Try a number from 1 to 4\n")
    #         self.welcome_screen()

    def log_into(self):
        os.system('clear')
        username = input('username: ')
        password = getpass.getpass('password: ')
        self.c.execute(SELECT_USERS)
        users = self.c.fetchall()

        for user in users:
            if username == user['username']:
                if encode_pass(password) == user['password']:
                    # self.c.execute(LOG_USER,
                    #                [user['id'], time.strftime('%Y-%m-%d %H:%M:%S')])
                    # self.db.commit()
                    return True

    def welcome_menu(self):
        os.system('clear')
        print('''Welcome to {}
            Now you have the following options:
            1) Show movies
            2) Show movie projections
            3) Make reservartions
            4) Cancel reservation
            5) Exit
            6) Help
            '''.format(self.name_of_cinema))
        choice = int(input("Choose an option: "))

        if choice == 1:
            self.list_movies()
        elif choice == 2:
            self.show_movie_projections(3)
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            self.exit()
        elif choice == 6:
            os.system('clear')
            self.help()
            print("Go")

    def list_movies(self):
        os.system('clear')
        self.c.execute(LIST_ALL_MOVIES)
        movies = self.c.fetchall()
        print("Here's a list of movies ordered by ascending order of rating to pick from: ")

        for movie in movies:
            print("[{}] - {} ({})".format(movie['ID'], movie['NAME'],
                                          movie['RATING']))

        print('''                   Now you can either:
                                1) see projections of a movie or
                                2) make a reservation''')
        choice = int(input('Choose an option:'))
        os.system('clear')

        if choice == 1:
            movie_id = input(
                "Choose movie [ID] and <date><YYYY-MM-DD>(optional): ")
            movie_id_and_date = movie_id.split(" ")
            if len(movie_id_and_date) < 2:
                self.show_movie_projections(movie_id)
            else:
                self.show_movie_projections(movie_id_and_date[0],
                                            movie_id_and_date[1])

        elif choice == 2:
            self.make_reservation()

    def show_movie_projections(self, movie_id, date=0):
        self.c.execute(GET_MOVIE_PROJECTIONS.format(movie_id))
        projections = self.c.fetchall()

        for projection in projections:
            print("Projections for movie '{}': ".format(projection['name']))
            print("[{}] - {} {} ({})"
                  .format(projection['id'], projection['PR_DATE'],
                          projection['PR_TIME'], projection['PR_TYPE']))

        # option = input("Do you want to go to the main menu and make a reservation? (Y/N)")
        # if option in ['Y', 'y']:
        #     self.welcome_menu()
        # else:
        #     os.system('Clear')
        #     self.exit()

    def make_reservation(self):
        os.system('clear')
        print ('''You have to log in order to make reservation!''')
        if self.log_into():
            self.c.execute(LIST_ALL_MOVIES)
            movies = self.c.fetchall()
            print(
                '''Here's a list of movies ordered by ascending order of rating to pick from: ''')

        for movie in movies:
            print("[{}] - {} ({})".format(movie['ID'], movie['NAME'],
                                          movie['RATING']))
        movie_id = input("Pick movie_id: ")

        self.show_movie_projections(movie_id)
        projection_id = input("pick projection id: ")
        self.print_seats(projection_id)

        seat = input("Pick a seat:")

    def print_seats(self, projection_id):
        self.c.execute(GET_FREE_SEATS_MATRIX.format(projection_id))
        taken_seats = self.c.fetchall()
        matrix = [['.'] * 10 for i in range(1, 11)]

        for co in taken_seats:
            matrix[co['rows']][co['cols']] = 'x'

        for i, row in enumerate(x):
            print(i, ' '.join(row))

    def help(self):
        self.c.execute(INSERT_USER,
                       ['Viktoriya Kertikova', encode_pass('vikiViki')])
        self.db.commit()
        print("bibi")

    def exit(self):
        os.system('clear')
        print("GOOD-BYE, SEE YOU AGAIN SOON!")
        return


def main():
    pass
    # menu = mainMenu()
    # menu.welcome_menu()
    # menu.welcome_menu()


if __name__ == "__main__":
    main()
