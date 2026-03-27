from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
import os

router = Router()

@router.message(Command("start"))
async def start_command(message: types.Message):
    webapp_url = os.getenv("WEBAPP_URL")
    
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(
                text="📚 Начать подготовку к ЕГЭ",
                web_app=WebAppInfo(url=f"{webapp_url}?user_id={message.from_user.id}")
            )],
            [KeyboardButton(text="ℹ️ О боте")],
            [KeyboardButton(text="📊 Моя статистика")]
        ],
        resize_keyboard=True
    )
    
    await message.answer(
        "🎓 Добро пожаловать в EGE Duolingo!\n\n"
        "Готовься к ЕГЭ в игровом формате:\n"
        "✅ Интерактивные задания\n"
        "✅ Персональный прогресс\n"
        "✅ Рейтинг и достижения\n\n"
        "Нажми на кнопку ниже, чтобы начать!",
        reply_markup=keyboard
    )

@router.message(lambda message: message.text == "ℹ️ О боте")
async def about(message: types.Message):
    await message.answer(
        "📖 <b>EGE Duolingo Bot</b>\n\n"
        "Интерактивная подготовка к ЕГЭ по всем предметам.\n"
        "Особенности:\n"
        "• Более 5000 заданий\n"
        "• Адаптивное обучение\n"
        "• Ежедневные цели\n"
        "• Рейтинг среди друзей\n\n"
        "Версия: 1.0\n"
        "Разработчик: @your_username"
    )

@router.message(lambda message: message.text == "📊 Моя статистика")
async def stats(message: types.Message):
    # Здесь будет логика получения статистики из БД
    await message.answer(
        "📊 <b>Ваша статистика</b>\n\n"
        "🏆 Уровень: 5\n"
        "⭐️ Очки: 1250\n"
        "📚 Пройдено тем: 12/50\n"
        "✅ Правильных ответов: 87%\n"
        "🔥 Серия: 7 дней\n\n"
        "Продолжайте в том же духе! 🚀"
    )
