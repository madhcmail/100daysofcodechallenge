import feedparser
from flask import Flask, render_template

app = Flask(__name__)
FEED_FILE = "newreleases.xml"
feeds = []
feed = feedparser.parse(FEED_FILE)
for entry in feed.entries:
    feeds.append(entry)


@app.route("/")
def print_feed():
    return render_template('feeds.html', feeds=feeds)


if __name__ == "__main__":
    app.run(debug=True)