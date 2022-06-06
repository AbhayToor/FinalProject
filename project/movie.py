# Movies by Raafay
from essentials import *

URL = "https://api.themoviedb.org/3"
API_Key = "bf12efc4be93154c3162660bbc44bba8"

def get_movie_genre():
    endpoint = f"{URL}/genre/movie/list?api_key={API_Key}&language=en-US"
    response = get_response(endpoint)
    amount_of_genres = len(response['genres'])
    list_of_genres = []
    for i in range(amount_of_genres - 1):
        list_of_genres.append(response['genres'][i]['name'])
    chosen_genre = chooseFromList("Choose a movie genre: ", list_of_genres)
    return chosen_genre