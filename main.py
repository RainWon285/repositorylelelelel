import requests
from bs4 import BeautifulSoup as bs

max_page = 402


def parsePage(page):
    response = requests.get(f"https://thedifference.ru/page/{page}/").text
    soup = bs(response, "html.parser")
    categoryItems = soup.find("div", class_="category-items")
    items = categoryItems.find_all("div", class_="item")

    title_url = []
    for item in items:
        entryTitle = item.find("div", class_="entry-title")
        title = entryTitle.find("a").text
        url = entryTitle.find("a").attrs["href"]

        title_url.append((title, url))

    return title_url
with open ("title.txt", "w", encoding="utf-8") as f:
    for page in range(1, max_page + 1):
        for title, url in parsePage(page):
            f.write(f"{title} | {url}\n")