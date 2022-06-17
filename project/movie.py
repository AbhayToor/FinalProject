# ==============================================================================
# Author: Abhay Toor & Raafay Qureshi
# Title: MusyFilm
# Description: This program ...
# ==============================================================================

from . import essentials
import random

URL = "https://api.themoviedb.org/3"
API_Key = "bf12efc4be93154c3162660bbc44bba8"


def get_movie_genre():
    ''' 
    () -> (str, int)
    Returns the movie genre and movie genre id

    Requires a movie library using an API 

    '''
    endpoint = f"{URL}/genre/movie/list?api_key={API_Key}&language=en-US"
    # Response is the access to the URL
    response = essentials.get_response(endpoint)
    amount_of_genres = len(response['genres'])
    list_of_genres = []
    list_of_genre_ids = []
    for i in range(amount_of_genres - 1):
        list_of_genres.append(response['genres'][i]['name'])
        list_of_genre_ids.append(response['genres'][i]['id'])
    # This prompts the user to pick a genre id
    # Which is saved as a variable for future use
    chosen_genre = essentials.chooseFromList(
        "Choose a movie genre: ", list_of_genres)
    index = list_of_genres.index(chosen_genre)
    genre_id = list_of_genre_ids[index]
    return chosen_genre, genre_id


def get_movies_by_genre(genre_id):
    '''
    (int) -> ()
    Get random movie from the dictionary of options

    Requires a index value to select option

    Parameters
        ----------
        genre_id : int
    '''
    endpoint = f"{URL}/discover/movie?api_key={API_Key}&with_genres={genre_id}&sort_by=popularity.desc"
    response = essentials.get_response(endpoint)
    # Data table retrieved from the URL
    total_pages = response['total_pages']
    # Default value of maximum number of pages is 500
    # Unless total pages are more than 500
    max_pages = 500 if total_pages > 500 else total_pages
    random_page = random.randint(1, max_pages)
    new_endpoint = endpoint + f"&page={random_page}"
    new_response = essentials.get_response(new_endpoint)
    random_movie = random.randrange(0, len(new_response["results"]))
    movie = new_response["results"][random_movie]
    print(
        f"Random movie generated: {movie['title']} released on {movie['release_date']} in {movie['original_language']}")


def movie_menu():
    '''
    () -> ()
    A void function that calls previous functions and prints out random movies

    '''
    genre, id = get_movie_genre()
    get_movies_by_genre(id)
