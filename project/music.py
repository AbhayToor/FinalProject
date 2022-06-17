# ==============================================================================
# Author: Abhay Toor & Raafay Qureshi
# Title: MusyFilm
# Description: This program ...
# ==============================================================================

from . import essentials
import json
import urllib.parse
import random

APIKey = "96fb158442ef3c34115a7fa8a1c9acdb"
URL = "http://ws.audioscrobbler.com/2.0/"


def get_music_genre():
    '''
    () -> (list)
    Outputting genres from a dictionary of options

    '''
    endpoint = URL + f"?method=tag.getTopTags&api_key={APIKey}&format=json"
    response = essentials.get_response(endpoint)
    genres = []
    for tag in response["toptags"]["tag"]:
        genres.append(tag["name"])
    return genres


def get_songs(genre):
    '''
    (int) -> (list)
    Returns a list of songs that have been extracted from dictionary

    Parameters
        ----------
        genre : int
    '''
    endpoint = URL + f"?method=chart.gettoptracks&api_key={APIKey}&format=json"
    response = essentials.get_response(endpoint)
    # Tracks is the index of the dictionary, and songs are the details of the tracks
    tracks = []
    for track in response["tracks"]["track"]:
        tracks.append((track["name"], track["artist"]["name"]))
    songs = []
    # Reiterating through the tracks twice to get needed information from two distinct URLs
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
        # Add every song and artist from dictionary based on genre
        for genre_dict in response['toptags']['tag']:
            if genre_dict['name'] == genre:
                songs.append((name, artist))
    return songs


def music_menu():
    '''
    () -> ()
    Prints out a random generated song based on user input

    Allows the user to choose a genre using an int value

    '''
    genres = get_music_genre()
    print("Pick one of the following genres")
    # Prints out the list of genres with numbers
    for i in range(18):
        print(f"{i + 1} {genres[i]}")
    print(" ")
    # User input to choose genre
    pick_genre = int(input("Choose a music genre: "))

    # Keeps asking the user until a valid input is given
    while pick_genre < 1 or pick_genre > 18:
        print("Invalid genre!")
        pick_genre = int(input("Choose a movie genre: "))
    genre = genres[pick_genre - 1]
    songs = get_songs(genre)
    choice = random.randrange(0, len(songs))
    song, artist = songs[choice]
    print(f"Random song generated: {song} by {artist}")
