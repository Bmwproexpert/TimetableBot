import asyncio
import logging
import sys
import parse

from aiogram import Dispatcher, Bot, F
from aiogram.types import Message
from aiogram.filters import CommandStart

TOKEN = "6765409876:AAGvW6oZeq_YB2mBcT-jliTO05mZzm5Z7aA"

dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    try:
        await message.answer("Hi <3\nI`m timetable bot")
    except:
        await message.answer("Something wrong")


@dp.message(F.text.lower() == "timetable")
async def timetable_get_handler(message: Message) -> None:
    try:
        await message.answer(parse.get_trains())
    except:
        print("Brrrr, I Can`t, *(")


async def main() -> None:
    global TOKEN
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
