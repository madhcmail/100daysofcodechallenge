import requests
import json
from pprint import pprint

results =[]

# pull the data from multiple pages using pagination and write it to json file.
for i in range(1,5):
    URL = f'https://api.themoviedb.org/3/discover/movie?api_key=<api_key>&page={i}'
    print("Downloading", URL)
    r = requests.get(URL)
    data = r.json()
    for item in data['results']:
        results.append(item)

# write the json data to file
with open("tmdb_movies_more.json", 'w') as f:
    json.dump(results, f)



