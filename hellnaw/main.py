import requests
from bs4 import BeautifulSoup as bs
import asyncio
import json
import aiogram

from os import getenv
import json


from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import Message

import getParser

TOKEN = ""
ADMIN_ID = 5269815078

bot = Bot(token=TOKEN)


dp = Dispatcher()
router = Router()

@router.message(Command("getgoods"))
async def asd(message: Message):

    try:
        l = message.text.split()[1]
        a = message.text.split()[2]
        goods = getParser.getGoodList(l, int(a))

        print(a)
        pop = ""

        for title, price ,url in goods:
            pop += f'<a href="https://msk.blokart.su{url}">{title.lstrip()}</a> |{price}р\n\n'

        pop += f"Страница: {a}"
        await message.answer(pop,parse_mode="HTML")
    except:
        await message.answer("Error")






if __name__ == "__main__":
    dp.include_router(router)
    dp.run_polling(bot)