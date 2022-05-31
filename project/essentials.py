import urllib.request

def chooseFromList(prompt, list):
    while True:
        try:
            print()
            for i, item in enumerate(list): print(f"{i + 1}. {item}")
            choice = int(input(f"\n{prompt}"))
            if choice >= 1 and choice <= len(list):
                return list[choice - 1]
            else:
                print("\nInvalid choice!")
        except:
            print("\nNot a valid number!")

def get_response(URL):
    payload = urllib.request.urlopen(URL)
    response = eval(payload.read())
    return response