import json

# Read the json file and process your data.
title_count =0
with open("tmdb_movies_more.json") as f:
    data = json.load(f)

for item in data:
    print(item["title"])
    title_count += 1 # trying to see how many results I get from the multiple page call.
print(title_count)
