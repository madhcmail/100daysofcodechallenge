import requests
import json
from pprint import pprint

total_results = []
for i in range(1,2):
    URL = f'https://api.themoviedb.org/3/discover/movie?api_key=<<api_key>>={i}'
    print("Downloading", URL)
    r = requests.get(URL)
    data = r.json()
    total_results = total_results + data['results']
    with open("tmdb_movies.json", 'w') as f:
        json.dump(total_results,f)
