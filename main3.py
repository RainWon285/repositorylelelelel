# TASK
# Спарсить товары их цену и ссылку
#
# https://catalog-sadovod.ru/

import requests
from bs4 import BeautifulSoup as bs

response = requests.get("https://www.labirint.ru/books/").text
soup = bs(response, "html.parser")

categoryItems = soup.find("div", class_="body-main-content-wrapper")
pages = categoryItems.find_all("a", class_="pagination-number__text")

maxPages = (int(pages[-1].text))

def parsePage(page):
    response1 = requests.get(f"https://www.labirint.ru/books/?page=1/").text
    soup1 = bs(response1, "html.parser")
    category = soup1.find("div", class_="products-row-outer")
    items = category.find_all("div", class_="product-cover")

    for item in items:
        name = item.find("a", class_="product-title-link").text
        print(name)


parsePage(1)

'''
for item in items1:
    productTitle = item.find("a", class_="product-title-link")

    #price
    productPrice = item.find("span", class_="ty-price-num")

    #url
    url = productTitle.attrs["href"]
    print(f"Текст: {productTitle.text} | Цена: {productPrice.text}р | Ссылка: {url}")
'''