# ==============================================================================
# Author: Abhay Toor & Raafay Qureshi
# Title: MusyFilm
# Description: This program allows the users to choose between two options,
#              movie or music. Using APIs it generates the top 18 genres
#              from the two options. Then, using random module and the API
#              a random top track and artist from that genre is generated.
# ==============================================================================

from . import music
from . import movie
from . import essentials


def main_menu():
    '''() -> 

    Takes user input from console based on options

    Prints the interface and validates the users input

    '''
    while True:
        print("Welcome to MusyFilm!\n")
        print("Options: \n")
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


if __name__ == "__main__":
    main_menu()
