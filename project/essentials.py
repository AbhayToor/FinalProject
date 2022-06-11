from urllib.request import urlopen
import json


def chooseFromList(prompt, list):
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
    response = urlopen(URL)
    return json.load(response)
