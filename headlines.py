from flask import Flask,render_template
import feedparser as fp
from flask import request
import json
import urllib2
import urllib

app = Flask(__name__)

DEFAULTS = {'publication':'bbc','city':'Islamabad,PK'}

RSS_FEED = {'bbc':'http://feeds.bbci.co.uk/news/rss.xml',
            'cnn':'http://rss.cnn.com/rss/edition.rss',
            'fox':'http://feeds.foxnews.com/foxnews/latest',
            'iol':'http://www.iol.co.za/cmlink/1.640',
            'sports':'https://www.geo.tv/rss/1/4.xml'}



@app.route("/")
def home():
    publication = request.args.get("publication")
    if not publication:
        publication = DEFAULTS['publication']
    articles = get_news(publication)
    city = request.args.get("city")
    if not city:
        city = DEFAULTS['city']
    weather = get_weather(city)
    return render_template("home.html",articles=articles,weather=weather)

def get_news(query):
    if not query or query.lower() not in RSS_FEED:
        publication = DEFAULTS['publication']
    else:
        publication = query.lower()
    feed = fp.parse(RSS_FEED[publication])
    return feed['entries']


def get_weather(query):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=4551584767a896532ac0c83dfede141a"
    query = urllib.quote(query)
    url = api_url.format(query)
    data = urllib2.urlopen(url).read()
    parsed = json.loads(data)
    weather = None
    if parsed.get("weather"):
        weather = {"description":parsed["weather"][0]["description"],
                   "temperature":parsed["main"]["temp"],
                   "city":parsed["name"],
                   "country":parsed['sys']['country']
                   }
    return weather
if __name__=='__main__':
    app.run()

