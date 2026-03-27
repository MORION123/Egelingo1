import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
import os

from handlers import start, webapp

load_dotenv()

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=os.getenv("8771751592:AAHVJR4xjomMF3eXwjVbjcpqmClT-qA_KSk"), parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    
    # Регистрация роутеров
    dp.include_router(start.router)
    dp.include_router(webapp.router)
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
