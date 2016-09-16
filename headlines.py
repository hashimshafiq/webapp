from flask import Flask,render_template
import feedparser as fp
from flask import request

app = Flask(__name__)
RSS_FEED = {'bbc':'http://feeds.bbci.co.uk/news/rss.xml',
            'cnn':'http://rss.cnn.com/rss/edition.rss',
            'fox':'http://feeds.foxnews.com/foxnews/latest',
            'iol':'http://www.iol.co.za/cmlink/1.640',
            'sports':'https://www.geo.tv/rss/1/4.xml'}



@app.route("/")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEED:
        publication = "sports"
    else:
        publication = query.lower()
    feed = fp.parse(RSS_FEED[publication])
    return render_template("home.html",articles=feed['entries'])
if __name__=='__main__':
    app.run()

