# ==============================================================================
# Author: Abhay Toor & Raafay Qureshi
# Title: MusyFilm
# Description: This program allows the users to choose between two options,
#              movie or music. Using APIs it generates the top 18 genres
#              from the two options. Then, using random module and the API
#              a random top track and artist from that genre is generated.
# ==============================================================================

from urllib.request import urlopen
import json


def chooseFromList(prompt, list):
    '''(int, list) -> str

    Takes in a string prompt and list and outputs the value of chosen index of the list

    Validates and ensures that prompt is a valid choice

    '''
    while True:
        try:
            for i, item in enumerate(list):
                print(f"\t{i + 1}. {item}")
            choice = int(input(f"\n{prompt}"))
            if choice >= 1 and choice <= len(list):
                return list[choice - 1]
            else:
                print("\nInvalid choice!")
        except:
            print("\nNot a valid number!")


def get_response(URL):
    '''() -> obj

    Returns the data set using the API

    '''
    response = urlopen(URL)
    return json.load(response)
