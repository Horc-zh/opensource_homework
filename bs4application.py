import requests, bs4
import csv
import json

url = "http://oscar-lab.org/people/~zren/files/puzzle.html"
res = requests.get(url)
res.encoding = res.apparent_encoding
doc = bs4.BeautifulSoup(res.text)
print(doc.prettify())

news = []
for tr in doc.tbody.find_all("tr"):
    tds = tr.find_all("td")
    ID = tds[0].text
    score = tds[1].text
    title = tds[2].text
    url = tds[2].a["href"]
    news.append({"ID": ID, "score": int(score), "title": title, "url": url})
higher_5 = [item["url"] for item in news if item["score"] > 5]
print(higher_5)


handle = open("news.csv", "w", newline="")
writer = csv.writer(handle)
header = ["ID", "score", "title", "url"]
rows = [[item[header[i]] for i in range(4)] for item in news]
writer.writerows([header] + rows)
handle.close()

print(news)

handle = open("news.json", "w")
json.dump(news, handle, ensure_ascii=False, indent=4)
handle.close()
