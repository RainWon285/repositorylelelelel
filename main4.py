import asyncio
import json
import aiogram

from os import getenv
import json


from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "6689895300:AAGax4A7_LjxIGiai8g4IRe4GzoN7GIJ-10"
ADMIN_ID = 5269815078

bot = Bot(token=TOKEN)


dp = Dispatcher()
router = Router()

def save_users(users):
    with open("users.json", "w") as outfile:
        json.dump(users, outfile)

def get_users():
    with open("users.json", "r") as infile:
        users = json.load(infile)
    return users
@router.message(Command("start"))
async def startMethod(message: Message):
    try:
        users = get_users()
    except:
        users = []

    if not message.from_user.id in users:
        users.append(message.from_user.id)
        save_users(users)
        await message.answer("Вы успешно подписались")
        return
    await message.answer("Вы уше подписаны")


@router.message(F.chat.id == ADMIN_ID)
async def dasdas(message: Message):
    try:
        users = get_users()
    except:
        users = []

    for user in users:
        await bot.send_message(chat_id=user, text=message.text)

if __name__ == "__main__":
    dp.include_router(router)
    dp.run_polling(bot)
