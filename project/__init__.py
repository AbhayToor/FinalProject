# functions for main menu
# import project to call it back
# project.foo(), normal function call

from music import *
from movie import *
from essentials import *

def main_menu():
    print("Welcome to MusyFilm")
    opening_choice = chooseFromList("Which option would you like to randomly generate?: ", ["movie", "music"])
    match (opening_choice):
        case "movie":
            genre = get_movie_genre()
            print(f"You chose the movie genre: {genre}")
        case "music":
            genre = get_music_genre()

if __name__ == "__main__":
    main_menu()