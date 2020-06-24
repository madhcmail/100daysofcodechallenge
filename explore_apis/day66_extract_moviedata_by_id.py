import json
import requests
from pprint import pprint

movie_results = []
for i in range(100, 150):
    URL = f'https://api.themoviedb.org/3/movie/{i}?api_key=<api_key>
    resp = requests.get(URL)
    data = resp.json()
    movie_results.append(data)

with open('movie_data.json', 'w') as f:
    json.dump(movie_results, f)

title_count = 0
with open('movie_data.json') as f:
    data = json.load(f)
    for item in data:
        if 'title' in item:  # check if title exists then it will print else move to next entry
            print(item["title"])
            print(item['overview'])
            print(item['release_date'])
            print(item['popularity'])
            print()
