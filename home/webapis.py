import requests


endpoint = "https://api.themoviedb.org/3/search/movie"
api_key = "57977be39193135c4e4e6c5fff02d212"


def movie_search(movie_title):
    query = movie_title.replace(" ", "+")
    params = {
        "query": query,
        "api_key": api_key
    }
    r = requests.get(url=endpoint, params=params)
    return r.json()
