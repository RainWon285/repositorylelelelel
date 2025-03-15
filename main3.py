# TASK
# Спарсить товары их цену и ссылку
#
# https://catalog-sadovod.ru/

import requests
from bs4 import BeautifulSoup as bs

response = requests.get("https://catalog-sadovod.ru/").text
soup = bs(response, "html.parser")

#grid-list
categoryItems = soup.find("div", class_="grid-list")

items = categoryItems.find_all("div", class_="ut2-gl__item")


for item in items:
    #product-title
    productTitle = item.find("a", class_="product-title")

    #price
    productPrice = item.find("span", class_="ty-price-num")

    #url
    url = productTitle.attrs["href"]
    print(f"Текст: {productTitle.text} | Цена: {productPrice.text}р | Ссылка: {url}")
