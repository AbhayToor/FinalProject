# functions for main menu
# import project to call it back
# project.foo(), normal function call

from . import music


def main_menu():
    while True:
        print("Options")
        print("\t(1) Quit")
        try:
            user_option = int(input("Enter option: "))
        except:
            print("Invalid option!")
            continue
        break
    music.get_genre()
