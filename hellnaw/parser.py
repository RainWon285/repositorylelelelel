import requests
from bs4 import BeautifulSoup as bs
import getParser

# ПОИСК ПО САЙТУ


def getByName(title, page = 1):
    response = requests.get(f"https://msk.blokart.su/search/?searchtext={title}&page={page}").text

    #Get pages
    pagesAmount = getParser.getPages(response)

    #getGoods
    goodsList = getParser.getGoodList(response)

    #for title, price in goodsList:
    #    print(f"{price} | {title}")





