import requests
import bs4

URL = f"https://www.foxnews.com/"


# pull the site
def pull_site():
    raw_site_page = requests.get(URL)
    raw_site_page.raise_for_status()
    return raw_site_page


# scrape the site for the required details
def scrape(site):
    headers_list = []

    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    html_header_list = soup.main.find_all('h2')

    for item in html_header_list:
        headers_list.append(item.getText())

    print("Fox Headlines: ")
    for idx, headers in enumerate(headers_list):
        print(f"{idx + 1} {headers}")


if __name__ == '__main__':
    site = pull_site()
    scrape(site)