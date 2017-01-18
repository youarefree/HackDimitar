from user_interface.main_menu import *

db = sqlite3.connect("cinema.db")

def main():
    menu = mainMenu("ARENA X")
    menu.welcome_menu()


if __name__ == "__main__":
    main()
