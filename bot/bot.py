from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor

API_TOKEN = "8771751592:AAHVJR4xjomMF3eXwjVbjcpqmClT-qA_KSk
"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# 🔘 Кнопка WebApp
kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="Открыть тренажёр",
        web_app=WebAppInfo(url="https://morion123.github.io/Egelingo1/")
    )]
])


# ▶️ Команда /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "📘 Тренажёр ЕГЭ по математике\n\nНажми кнопку ниже 👇",
        reply_markup=kb
    )


# 📥 Получение данных из WebApp
@dp.message_handler(content_types=types.ContentType.WEB_APP_DATA)
async def web_app_data(message: types.Message):
    await message.answer(f"📊 Результат: {message.web_app_data.data}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
