import requests
import json

query = input("Enter your query: ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-10-12&language=en&sortBy=publishedAt&apiKey=  (#enter your Api key )"

a = requests.get(url)
news = json.loads(a.text)
for articles in news["articles"]:
    print(articles["title"])
    print(articles["description"])
    print(articles["url"])
    print("------------------------------------")
