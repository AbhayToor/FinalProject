# Movies by Raafay
from essentials import *
import random

URL = "https://api.themoviedb.org/3"
API_Key = "bf12efc4be93154c3162660bbc44bba8"

def get_movie_genre():
    endpoint = f"{URL}/genre/movie/list?api_key={API_Key}&language=en-US"
    response = get_response(endpoint)
    amount_of_genres = len(response['genres'])
    list_of_genres = []
    list_of_genre_ids = []
    for i in range(amount_of_genres - 1):
        list_of_genres.append(response['genres'][i]['name'])
        list_of_genre_ids.append(response['genres'][i]['id'])
    chosen_genre = chooseFromList("Choose a movie genre: ", list_of_genres)
    index = list_of_genres.index(chosen_genre)
    genre_id = list_of_genre_ids[index]
    return chosen_genre, genre_id

def get_movies_by_genre(genre_id):
    endpoint = f"{URL}/discover/movie?api_key={API_Key}&with_genres={genre_id}&sort_by=popularity.desc"
    response = get_response(endpoint)
    total_pages = response['total_pages']
    max_pages = 500 if total_pages > 500 else total_pages
    random_page = random.randint(1,max_pages)
    new_endpoint = endpoint + f"&page={random_page}"
    new_response = get_response(new_endpoint)
    results = new_response['results']
    random_result = random.choice(results)
    title = random_result['title']
    overview = random_result['overview']
    release_date = random_result['release_date']
    adult = random_result['adult']
    print(f"\nThe movie you got is titled: {title}\n\nOverwiew of movie: {overview}\n\nRelease Date: {release_date}\n\nAdult Rated Film: {adult}")

def movie_menu():
    while True:
        genre, id = get_movie_genre()
        print(f"You chose the movie genre: {genre}")
        while True:
            get_movies_by_genre(id)
            replay_same_genre = chooseFromList(f"Would you like to replay with the same genre? {genre}: ", ["True", "False"])
            if replay_same_genre == "False":
                break
        replay_movie = chooseFromList("Would you like to replay for another movie in another genre?: ", ["True", "False"])
        if replay_movie == "False":
            break