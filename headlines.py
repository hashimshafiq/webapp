from flask import Flask
import feedparser as fp
app = Flask(__name__)
BBC_FEED = "https://www.geo.tv/rss/1/1.xml"

@app.route("/")
def get_news():
    feed = fp.parse(BBC_FEED)
    first_article = feed['entries'][0]
    return """<html
            <body>
            <h1>GEO NEWS Headlines</h1> <br />
            <b>{0}</b>  <br />
            {1} <br />
            <i>{2}</i> <br />
            <p></p> <br />
            </body>
            </html>""".format(first_article.get("title"),first_article.get("link"),first_article.get("description").encode('ascii','ignore').decode('ascii'))


if __name__=='__main__':
    app.run()

