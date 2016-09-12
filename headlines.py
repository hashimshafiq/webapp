from flask import Flask,render_template
import feedparser as fp
app = Flask(__name__)
RSS_FEED = {'world':'https://www.geo.tv/rss/1/0.xml',
            'pakistan':'https://www.geo.tv/rss/1/1.xml',
            'world1':'https://www.geo.tv/rss/1/2.xml',
            'business':'https://www.geo.tv/rss/1/3.xml',
            'sports':'https://www.geo.tv/rss/1/4.xml'}



@app.route("/<publication>")
def get_news(publication="pakistan"):
    feed = fp.parse(RSS_FEED[publication])
    first_article = feed['entries'][0]
    return render_template("home.html",title=first_article.get("title"),link=first_article.get("link"),pubDate=first_article.get("pubDate"),description=first_article.get("description"))

if __name__=='__main__':
    app.run()

