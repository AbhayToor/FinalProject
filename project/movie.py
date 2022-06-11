# Movies by Raafay

from . import essentials
import random

URL = "https://api.themoviedb.org/3"
API_Key = "bf12efc4be93154c3162660bbc44bba8"


def get_movie_genre():
    endpoint = f"{URL}/genre/movie/list?api_key={API_Key}&language=en-US"
    response = essentials.get_response(endpoint)
    amount_of_genres = len(response['genres'])
    list_of_genres = []
    list_of_genre_ids = []
    for i in range(amount_of_genres - 1):
        list_of_genres.append(response['genres'][i]['name'])
        list_of_genre_ids.append(response['genres'][i]['id'])
    chosen_genre = essentials.chooseFromList(
        "Choose a movie genre: ", list_of_genres)
    index = list_of_genres.index(chosen_genre)
    genre_id = list_of_genre_ids[index]
    return chosen_genre, genre_id


def get_movies_by_genre(genre_id):
    endpoint = f"{URL}/discover/movie?api_key={API_Key}&with_genres={genre_id}&sort_by=popularity.desc"
    response = essentials.get_response(endpoint)
    total_pages = response['total_pages']
    max_pages = 500 if total_pages > 500 else total_pages
    random_page = random.randint(1, max_pages)
    new_endpoint = endpoint + f"&page={random_page}"
    new_response = essentials.get_response(new_endpoint)
    random_movie = random.randrange(0, len(new_response["results"]))
    movie = new_response["results"][random_movie]
    print(
        f"{movie['title']} released on {movie['release_date']} in {movie['original_language']}")


def movie_menu():
    genre, id = get_movie_genre()
    get_movies_by_genre(id)
