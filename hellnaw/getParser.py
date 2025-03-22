import requests
from bs4 import BeautifulSoup as bs


def getPages(title, page= 1):
    response = requests.get(f"https://msk.blokart.su/search/?searchtext={title}&page={page}").text
    soup = bs(response, "html.parser")
    categoryItems = soup.find("div", class_="b-nav")
    items = categoryItems.find_all("a", class_="b-nav__item")


    i = []
    for item in items:
        i.append(item.text)

    return i

def getGoodList(title, page= 1 ):

    i = []

    response = requests.get(f"https://msk.blokart.su/search/?searchtext={title}&page={page}").text
    soup = bs(response, "html.parser")
    categoryItems = soup.find("div", class_="b-catalog__wrap")
    items = categoryItems.find_all("div", class_="good-item__wrap")

    for item in items:
        price = item.find("span", class_="b-price")
        title = item.find("a", class_="good-item__title-link")
        url = item.find("a", class_="good-item__title-link").attrs["href"]


        i.append((title.text, price.text, url))
    return i