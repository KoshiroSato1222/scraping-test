import requests
import bs4

r = requests.get("https://www.oreilly.co.jp/ebook/")

soup = bs4.BeautifulSoup(r.text, "html.parser")
table = soup.find("table")
release_title = table.findAll("h3")
print(table)