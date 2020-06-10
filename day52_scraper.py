import requests
from bs4 import BeautifulSoup
import csv

source = requests.get("https://coreyms.com").text

soup = BeautifulSoup(source, 'html.parser')

csv_file = open("scrape_date.csv", 'w')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):

    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)
    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f"https://www.youtube.com/watch?v={vid_id}"

    except Exception as e:
        yt_link = None

    print(yt_link)
    print()

    csv_writer.writerow([headline,summary,yt_link])

csv_file.close