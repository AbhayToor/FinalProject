from urllib.request import urlopen
import json

def chooseFromList(prompt, list):
    while True:
        try:
            for i, item in enumerate(list):
                print(f"{i + 1}. {item}")
            choice = input(f"\n{prompt}")
            for option in list:
                if choice.lower() == option.lower():
                    return option
            castedChoice = int(choice)
            if castedChoice >= 1 and castedChoice <= len(list):
                return list[castedChoice - 1]
            else:
                print("\nInvalid choice!")
        except:
            print("\nInvalid choice!")


def get_response(URL):
    response = urlopen(URL)
    return json.load(response)
