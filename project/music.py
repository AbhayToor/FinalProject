from . import essentials
import json
import urllib.parse

APIKey = "96fb158442ef3c34115a7fa8a1c9acdb"
URL = "http://ws.audioscrobbler.com/2.0/"


def get_music_genre():
    endpoint = URL + f"?method=tag.getTopTags&api_key={APIKey}&format=json"
    response = essentials.get_response(endpoint)
    genres = []
    for tag in response["toptags"]["tag"]:
        genres.append(tag["name"])
    return genres


def get_songs(genre):
    endpoint = URL + f"?method=chart.gettoptracks&api_key={APIKey}&format=json"
    response = essentials.get_response(endpoint)
    tracks = []
    for track in response["tracks"]["track"]:
        tracks.append((track["name"], track["artist"]["name"]))
    songs = []
    for name, artist in tracks:
        name = urllib.parse.quote(name)
        artist = urllib.parse.quote(artist)
        endpoint = URL + \
            f"?method=track.getTopTags&api_key={APIKey}&artist={artist}&track={name}&format=json&user=RJ"
        response = essentials.get_response(endpoint)
        print(response)
        # Todo: Check through all the top tags from response; use response to get the top tags from the response objects
        # Todo: If any of the toptags in response are genre add song and artist to song list


def music_menu():
    genres = get_music_genre()
    print("Pick one of the following genres")
    for i in range(8):
        print(f"{i + 1} {genres[i]}")
    pick_genre = int(input("Choose a genre: "))

    while pick_genre < 1 or pick_genre > 8:
        print("Invalid genre")
        pick_genre = int(input("Choose a genre: "))
    genre = genres[pick_genre - 1]
    songs = get_songs(genre)
