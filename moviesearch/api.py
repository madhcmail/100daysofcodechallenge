import requests

def find_movie_by_title(keyword):
    URL = f"https://movieservice.talkpython.fm/api/search/{keyword}"

    resp = requests.get(URL)
    resp.raise_for_status()

    results = resp.json()
    return results.get('hits')

