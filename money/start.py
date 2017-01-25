import sql_manager
import getpass
from hashing import *
import os


def main_menu():

    while True:
        print ('''Welcome to our bank service system!
                You have the following options:
                1. Register
                2. Log in
                3. Help
                4. Exit
                ''')
        choice = int(input("Input your choice: "))

        if choice == 1:
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")

            while not validate_pass(password, username):

                print("Password must contain 1 uppercase and lowercase letter at\
                        least and one special symbol and must\
                         differ from username")
                password = getpass.getpass("Enter your password: ")
            else:
                verify_pass = getpass.getpass("Verify password: ")

                if verify_pass == password:
                    sql_manager.register(username, password)
                    print("Registration Successfull")
                else:
                    print("Password mismatch. Try again")

        elif choice == 2:
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")

            logged_user = sql_manager.login(username, password)

            if logged_user:
                logged_menu(logged_user)
            else:
                print("Login failed")

        elif choice == 3:
            os.system("clear")
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif choice == 4:
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    while True:
        print('''Hi, {}
                Now you have the following options:
                1) Info
                2) Change pass
                3) Show message
                4) Change message
                5) DEPOSIT MONEY
                6) WITHDRAW MONEY
                7) DISPLAY CURRENT BALANCE
                8) Help
                9) log out
                '''.format(logged_user.get_username()))
        choice = int(input("Choose an option: "))

        if choice == 1:
            os.system('clear')
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')
        elif choice == 2:
            new_pass = getpass.getpass("Enter your new password: ")
            verify_pass = getpass.getpass("Enter your new password again!: ")
            if new_pass == verify_pass and validate_pass(new_pass, logged_user.get_username()):
                    sql_manager.change_pass(new_pass, logged_user)
            else:
                print("Invalid password")
        elif choice == 3:
            os.system('clear')
            print(logged_user.get_message())
        elif choice == 4:
            os.system('clear')
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)
        elif choice == 5:
            amount = input("How much do you want to deposit?")
            sql_manager.deposit(amount, logged_user)
            print("You have successfully added {} $ to your account".format(amount))
        elif choice == 6:
            os.system('clear')
            amount = input("How much do you want to withdraw: ")
            if sql_manager.withdraw(amount):
                print("Here are your {} $".format(amount))
            else:
                print("You don't have that kind of money")
        elif choice == 7:
            os.system('clear')
            print("Your balance is:" + str(logged_user.get_balance()) + '$')
        elif choice == 8:
            print('''Info - for showing account info
            Change pass - for changing passowrd
            Change message - for changing users message
            Show message - for showing users message
            ''')
        elif choice == 9:
            break


def main():
    # sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
