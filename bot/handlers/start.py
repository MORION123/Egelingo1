from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
import os

router = Router()

# Ваш WebApp URL
WEBAPP_URL = "https://morion123.github.io/Egelingo1"
# Ваш API токен
BOT_TOKEN = "8771751592:AAHVJR4xjomMF3eXwjVbjcpqmClT-qA_KSk"

def get_main_keyboard(webapp_url: str, user_id: int = None):
    """Создание главной клавиатуры"""
    webapp_url_with_user = f"{webapp_url}?user_id={user_id}" if user_id else webapp_url
    
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="📚 Начать подготовку к ЕГЭ",
                    web_app=WebAppInfo(url=webapp_url_with_user)
                )
            ],
            [
                KeyboardButton(text="ℹ️ О боте"),
                KeyboardButton(text="📊 Моя статистика")
            ],
            [
                KeyboardButton(text="🎯 Ежедневная цель"),
                KeyboardButton(text="🏆 Рейтинг")
            ]
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие..."
    )
    return keyboard

@router.message(Command("start"))
async def start_command(message: types.Message):
    """Обработчик команды /start"""
    user_id = message.from_user.id
    username = message.from_user.first_name
    
    welcome_text = (
        f"🎓 <b>Добро пожаловать в EGE Duolingo, {username}!</b>\n\n"
        "🚀 <b>Интерактивная подготовка к ЕГЭ</b>\n"
        "Преврати подготовку к экзаменам в увлекательную игру!\n\n"
        "✨ <b>Что вас ждет:</b>\n"
        "✅ <b>5000+</b> заданий по всем предметам\n"
        "🎮 <b>Игровой формат</b> с системой уровней\n"
        "📈 <b>Персональный</b> трек обучения\n"
        "🏅 <b>Достижения</b> и рейтинг\n"
        "🔥 <b>Ежедневные</b> цели и серии\n\n"
        f"🌐 <b>Наш сайт:</b> {WEBAPP_URL}\n\n"
        "👇 <b>Нажмите на кнопку ниже, чтобы начать!</b>"
    )
    
    await message.answer(
        welcome_text,
        reply_markup=get_main_keyboard(WEBAPP_URL, user_id),
        parse_mode="HTML"
    )

@router.message(lambda message: message.text == "ℹ️ О боте")
async def about_bot(message: types.Message):
    """Информация о боте"""
    about_text = (
        "📖 <b>EGE Duolingo Bot</b> - версия 2.0\n\n"
        "🎯 <b>Наша миссия:</b>\n"
        "Сделать подготовку к ЕГЭ доступной, эффективной и увлекательной.\n\n"
        "⚙️ <b>Возможности:</b>\n"
        "• <b>Адаптивное обучение</b> - задания подбираются под ваш уровень\n"
        "• <b>Система повторений</b> - забытый материал автоматически возвращается\n"
        "• <b>Подробная статистика</b> - отслеживайте прогресс\n"
        "• <b>Соревнования</b> - соревнуйтесь с друзьями\n"
        "• <b>Офлайн-режим</b> - учитесь без интернета\n\n"
        "📚 <b>Доступные предметы:</b>\n"
        "Математика, Русский язык, Физика, Химия,\n"
        "История, Информатика, Биология, География\n\n"
        f"🌐 <b>Наш сайт:</b> {WEBAPP_URL}\n\n"
        "💡 <b>Совет:</b> Занимайтесь ежедневно по 15-20 минут\n"
        "для достижения наилучших результатов!\n\n"
        "📞 <b>Поддержка:</b> @ege_duolingo_support"
    )
    
    await message.answer(about_text, parse_mode="HTML")

@router.message(lambda message: message.text == "📊 Моя статистика")
async def user_stats(message: types.Message):
    """Показать статистику пользователя"""
    username = message.from_user.first_name
    
    stats_text = (
        f"📊 <b>Статистика пользователя</b>\n"
        f"👤 {username}\n\n"
        f"🏆 <b>Уровень:</b> 5\n"
        f"⭐️ <b>Всего очков:</b> 1,250 XP\n"
        f"📚 <b>Пройдено уроков:</b> 42\n"
        f"✅ <b>Правильных ответов:</b> 87%\n"
        f"🔥 <b>Серия:</b> 7 дней\n"
        f"🎯 <b>Выполнено целей:</b> 5/7\n\n"
        f"📈 <b>Прогресс по предметам:</b>\n"
        f"• Математика: ▰▰▰▰▰▰▰▰▰▰ 85%\n"
        f"• Русский язык: ▰▰▰▰▰▰▰▰▰▰ 72%\n"
        f"• Физика: ▰▰▰▰▰▰▰▰▰▰ 45%\n\n"
        f"🏅 <b>Достижения:</b>\n"
        f"🏆 Первый урок (✅)\n"
        f"⭐️ 1000 XP (✅)\n"
        f"🔥 7-дневная серия (✅)\n"
        f"📚 Мастер математики (🔒)\n\n"
        f"<i>Продолжайте учиться, чтобы открыть новые достижения!</i>"
    )
    
    await message.answer(stats_text, parse_mode="HTML")

@router.message(lambda message: message.text == "🎯 Ежедневная цель")
async def daily_goal(message: types.Message):
    """Показать ежедневную цель"""
    await message.answer(
        "🎯 <b>Ваша ежедневная цель</b>\n\n"
        "📊 Прогресс на сегодня:\n"
        "▰▰▰▰▰▰▰▰▰▰ 75%\n\n"
        "✅ Выполнено: 75/100 XP\n"
        "🔥 Серия: 7 дней\n\n"
        "Осталось набрать 25 XP для выполнения цели!\n"
        "Продолжайте учиться! 💪",
        parse_mode="HTML"
    )

@router.message(lambda message: message.text == "🏆 Рейтинг")
async def leaderboard(message: types.Message):
    """Показать таблицу лидеров"""
    leaderboard_text = (
        "🏆 <b>Топ-10 пользователей</b>\n\n"
        "1️⃣ <b>Иван</b> - 2500 XP (Уровень 8)\n"
        "2️⃣ <b>Мария</b> - 2100 XP (Уровень 7)\n"
        "3️⃣ <b>Алексей</b> - 1850 XP (Уровень 6)\n"
        "4️⃣ <b>Екатерина</b> - 1700 XP (Уровень 6)\n"
        "5️⃣ <b>Дмитрий</b> - 1550 XP (Уровень 5)\n"
        "6️⃣ <b>Анна</b> - 1400 XP (Уровень 5)\n"
        "7️⃣ <b>Сергей</b> - 1300 XP (Уровень 4)\n"
        f"8️⃣ <b>{message.from_user.first_name}</b> - 1250 XP (Уровень 5) 👈 Вы\n"
        "9️⃣ <b>Ольга</b> - 1100 XP (Уровень 4)\n"
        "🔟 <b>Павел</b> - 950 XP (Уровень 3)\n\n"
        "📈 <i>Поднимитесь в рейтинге, выполняя больше заданий!</i>"
    )
    
    await message.answer(leaderboard_text, parse_mode="HTML")
