import requests
import json
from pprint import pprint

# read a json file in to python data object
with open('mount-data.json') as f:
    data = json.load(f)

# parse through the nested dict and get the names of the mounts
for item in data['mounts']['collected']:
    print(item['name'])

# get the list of dictionaries for the mount names that are flying

is_flying= []

for item in data['mounts']['collected']:
    if item['isFlying']:
        is_flying.append(item)

# print the values for the name key from the is_flying list

for item in is_flying:
    print(item['name'])

