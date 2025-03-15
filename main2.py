import requests
from bs4 import BeautifulSoup as bs

response = requests.get("https://thedifference.ru/").text
soup = bs(response, "html.parser")
categoryItems = soup.find("div", class_="sidebar")
items = categoryItems.find_all("div", class_="name")

for item in items:
    url = item.find("a").attrs["href"]
    print(f"{item.text} | {url}")

