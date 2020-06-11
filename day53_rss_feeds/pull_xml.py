import requests

URL = "https://store.steampowered.com/feeds/newreleases.xml"

if __name__=='__main__':
    r = requests.get(URL)
    with open("newreleases.xml", "wb") as f:
        f.write(r.content)