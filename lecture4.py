import feedparser
import pprint

date = feedparser.parse("https://news.yahoo.co.jp/rss/topics/domestic.xml")
print(pprint.pprint(date["entries"]))
print(len(date["entries"]))

for i in range(0, len(date["entries"])):
    print(date["entries"][i]["title"])
    print(date["entries"][i]["published"])
    print(date["entries"][i]["link"])
