# ==============================================================================
# Author: Abhay Toor & Raafay Qureshi
# Title: MusyFilm
# Description: This program ...
# ==============================================================================

# functions for main menu
# import project to call it back
# project.foo(), normal function call

from . import music
from . import movie
from . import essentials


def main_menu():
    while True:
        print("Welcome to MusyFilm!\n")
        print("Options: ")
        print("\t Music")
        print("\t Movie")
        try:
            opening_choice: str = (
                input("Are you interested in Movies or Music: ")).lower().strip()
            if opening_choice == "music":
                music.music_menu()
            elif opening_choice == "movie":
                movie.movie_menu()
        except:
            print("Invalid Option!")
            continue


def second_menu():
    while True:
        print("What do you want to do?")


if __name__ == "__main__":
    main_menu()
