# ==============================================================================
# Author: Abhay Toor & Raafay Qureshi
# Title: MusyFilm
# Description: This program ...
# ==============================================================================

from urllib.request import urlopen
import json


def chooseFromList(prompt, list):
    '''
    (int, list) -> (str)  

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
    '''
    () -> (str)

    Returns the data set using the API

    '''
    response = urlopen(URL)
    return json.load(response)
