# functions for main menu
# import project to call it back
# project.foo(), normal function call

import music
import movie
from essentials import *

def main_menu():
    print("Welcome to MusyFilm")
    while True:
        opening_choice = chooseFromList("Which option would you like to randomly generate?: ", ["movie", "music"])
        match (opening_choice):
            case "movie":
                movie.movie_menu()
            case "music":
                music.music_menu()
        replay_randomizer = chooseFromList("Would you like to replay the randomizer?: ", ["True", "False"])
        if replay_randomizer == "False":
            break


if __name__ == "__main__":
    main_menu()