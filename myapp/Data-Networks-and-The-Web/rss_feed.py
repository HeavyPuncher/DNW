from flask import Flask
import feedparser
from random import randint

app = Flask(__name__)

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"

@app.route("/")
def headline():
	feed = feedparser.parse(BBC_FEED)
	ali = randint(0,9)
	article = feed['entries'][ali]
	return """<html>
	<body>
	<h1> BBC Headline </h1>
	<b>{0}</b></br>
	<i>{1}</i></br>
	<p>{2}</p></br>
	</body>
	</html>""".format(article.get("title"),
	article.get("published"), article.get("summary"))


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)


