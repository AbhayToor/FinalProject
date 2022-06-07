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


# print(get_response("http://ws.audioscrobbler.com/2.0/"))

APIKey = "96fb158442ef3c34115a7fa8a1c9acdb"
URL = "http://ws.audioscrobbler.com/2.0/"
endpoint = URL + f"?method=tag.getTopTags&api_key={APIKey}&format=json"
response = get_response(endpoint)
print(response)
