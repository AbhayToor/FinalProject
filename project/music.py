import urllib.request

APIKey = "96fb158442ef3c34115a7fa8a1c9acdb"
URL = "http://ws.audioscrobbler.com/2.0/"


def get_genre():
    endpoint = URL + f"?method=tag.getTopTags&api_key={APIKey}&format=json"
    response = urllib.request.urlopen(endpoint)
    print(str(response.read()))
