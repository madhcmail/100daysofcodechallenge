import requests
import collections
from typing import List

Podcast = collections.namedtuple('Podcast', 'category, id, url, title, description')

# function to search teh podcast by keyword
def search_talkpython_by_keyword(keyword: str) -> List[Podcast]:
    url = f'https://search.talkpython.fm/api/search?q={keyword}'

    resp = requests.get(url)
    resp.raise_for_status()

    # converting the json to python dictionary
    r_dict = resp.json()
    podcasts = []  # appending the tuples to list
    for r in r_dict.get('results'):
        podcasts.append(Podcast(**r))

    return podcasts