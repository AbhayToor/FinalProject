import essentials
import urllib.parse
import random

APIKey = "96fb158442ef3c34115a7fa8a1c9acdb"
URL = "http://ws.audioscrobbler.com/2.0/"


def get_music_genre():
    """ (list)
    Returns the genres from the API dictionary
    """
    endpoint = URL + f"?method=tag.getTopTags&api_key={APIKey}&format=json"
    response = essentials.get_response(endpoint)
    genres = []
    for tag in response["toptags"]["tag"]:
        genres.append(tag["name"])
    return genres


def get_songs(genre):
    """ (list)
    Gets name of songs and artist from dictionary
    """
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
    for name, artist in tracks:
        name_quoted = urllib.parse.quote(name)
        artist_quoted = urllib.parse.quote(artist)
        endpoint = URL + \
            f"?method=track.getTopTags&api_key={APIKey}&artist={artist_quoted}&track={name_quoted}&format=json&user=RJ"
        response = essentials.get_response(endpoint)
        for genre_dict in response['toptags']['tag']:
            if genre_dict['name'] == genre:
                songs.append((name, artist))
    return songs


def music_menu():
    """ (string) -> int
    Gets user input for genre and validates the input
    >>> Music
    '1 rock'
    '2 electronic'
    '3 seen live'
    '4 alternative'
    '5 indie'
    '6 pop'
    '7 female vocalists'
    '8 metal' 
    """
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
    choice = random.randrange(0, len(songs))
    song, artist = songs[choice]
    print(f"{song} by {artist}")
