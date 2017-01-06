import getpass
from user import *
import sqlite3
from settings import DB_NAME
from hashing import *
import os
from queries import *

db = sqlite3.connect(DB_NAME)
db.row_factory = sqlite3.Row
c = db.cursor()


class mainMenu():

    def __init__(self, name_of_hospital):
        self.name = name_of_hospital

    def welcome_screen(self):
        os.system('clear')
        print ('''Welcome to {}!
                You have the following options:
                1. To log into the hospital's system
                2. Register
                3. Get help
                4. Exit
                '''.format(self.name))
        choice = int(input("Input your choice: "))
        if choice == 1:
            self.log_into()
        elif choice == 2:
            self.registartion()
        elif choice == 3:
            self.help()
        elif choice == 4:
            self.exit()
        else:
            os.system('clear')
            print("No such option. Try a number from 1 to 4\n")
            welcome_screen()

    def log_into(self):
        os.system('clear')
        username = input('username: ')
        password = getpass.getpass('password: ')
        c.execute(SELECT_USERS)
        users = c.fetchall()

        for user in users:
            if username == user['username']:
                if encode_pass(password) == user['password']:
                    c.execute(INTO_THE_SYSTEM.format(user['id']))
                    db.commit()
                    self.validate_login(user)
            # os.system('clear')
            # print("Incorrect Password or Username")
            # self.welcome_screen()

        # print("Incorrect username")
        # welcome_screen()

    def patient_login_menu(self, user):
        print('''Hi, {}
            You're Logged in as a patient!
            Now you have the following options:
            1) see the free hours of your doctor
            2) reserve hour for visitation
            3) stay at the hospital for an injury
            4) see the academic title of your doctor
            5) list your hospital stays
            6) change your doctor
            7) change your username and/or age
            8) log out
            '''.format(user['username']))
        choice = int(input("Choose an option: "))

        if choice == 1:
            os.system('clear')
            self.list_free_hours_of_doctor(user)
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            pass
        elif choice == 8:
            self.log_out(user)

    def doctor_login_menu(self, user):
        c.execute(SELECT_ACADEMIC_TITLE.format(user['id']))
        academic_title = c.fetchone()

        print ('''Hi, {}
            You're a {}!
            You have the abilities to:
            1) list all of your patients
            2) add hours for visitation
            3) delete free hours of visitation
            4) see the room and the duration of
            hospital stays per each of your patients
            5) change your username and/or age
            6) raise into the hospital hierarchy
            7) log out
            >
            '''.format(user['username'], academic_title['academic_title']))
        choice = int(input("Choose an option: "))

        if choice == 1:
            os.system('clear')
            self.list_all_patients(user)
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            self.list_stays_of_patients(user)
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            os.system('clear')
            self.log_out(user)

    def registartion(self):
        os.system('clear')
        print("Registration...")
        username = input("Input username: ")
        pwd = getpass.getpass("Password:")
        again_pwd = getpass.getpass("Input password again")

        while again_pwd != pwd:
            os.system('clear')
            print('You have a password mismatch!')
            again_pwd = getpass.getpass('Input again:')

        while not validate_pass(pwd):
            os.system('clear')
            print("Incorrect pass... Input again. Must contain at least 1 uppercase letter, 1 lower case and 1 digit")
            pwd = getpass.getpass("Password:")
            again_pwd = getpass.getpass("Input password again")

        age = input('age: ')
        gender = input('gender: ')
        user = User()

        if user.initialise(username, pwd, age, gender):
            c.execute(REGISTER_IN_SYSTEM, [username, encode_pass(pwd), age])
            db.commit()
            self.validate_login(user)

    def help(self):
        self.welcome_screen()

    def exit(self):
        os.system('clear')
        print('Good-Bye! Come back again!')
        return

    def log_out(self, user):
        c.execute(OUT_OF_THE_SYSTEM.format(user['id']))
        db.commit()
        self.welcome_screen()

    def list_all_patients(self, user):
        os.system('clear')
        c.execute(GET_PATIENTS_OF_DOCTOR.format(user['id']))
        patients = c.fetchall()
        print("Here's a list of all your patients {}: ".format(user['username']))

        for patient in patients:
            print(patient['username'])

        choice = input("Do something else? Y/N\n")
        if choice in ['Y', 'y']:
            self.login_menu()
        else:
            return

    def list_stays_of_patients(self, user):
        os.system('clear')
        c.execute(LIST_ROOM_AND_DURATION_OF_PATIENT.format(user['id']))
        durations = c.fetchall()

        for duration in durations:
            print("Room: {}, Start Date: {}, End Date: {}".format(duration['room'],duration['startdate'],duration["enddate"]))
        self.validate_login(user)

    def list_free_hours_of_doctor(self, user):
        os.system('clear')
        doctor_id = SELECT_DOCTOR_ID.format(user['id'])
        c.execute(LIST_FREE_HOURS_OF_DOCTOR.format(doctor_id))
        free_hours = c.fetchone()
        print(free_hours(['FROM_TO']))


    def validate_login(self, user):
        if 'Dr.' not in str(user['username']):
            self.patient_login_menu(user)
        else:
            self.doctor_login_menu(user)


def main():
    menu = mainMenu("JIVO")
    menu.welcome_screen()



if __name__ == '__main__':
    main()
