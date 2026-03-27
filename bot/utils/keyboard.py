from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)

# Ваш WebApp URL
WEBAPP_URL = "https://morion123.github.io/Egelingo1"

def get_main_keyboard(webapp_url: str = WEBAPP_URL, user_id: int = None):
    """Главная клавиатура с WebApp кнопкой"""
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

def get_subjects_keyboard():
    """Клавиатура выбора предметов"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📐 Математика", callback_data="subject_math"),
                InlineKeyboardButton(text="📖 Русский язык", callback_data="subject_russian")
            ],
            [
                InlineKeyboardButton(text="⚛️ Физика", callback_data="subject_physics"),
                InlineKeyboardButton(text="🧪 Химия", callback_data="subject_chemistry")
            ],
            [
                InlineKeyboardButton(text="🌍 История", callback_data="subject_history"),
                InlineKeyboardButton(text="💻 Информатика", callback_data="subject_informatics")
            ],
            [
                InlineKeyboardButton(text="📚 Биология", callback_data="subject_biology"),
                InlineKeyboardButton(text="🗺️ География", callback_data="subject_geography")
            ],
            [
                InlineKeyboardButton(text="🌐 Открыть сайт", url=WEBAPP_URL)
            ]
        ]
    )
    return keyboard

def get_lesson_keyboard(lesson_id: int, total_questions: int):
    """Клавиатура для урока"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Ответить", callback_data=f"answer_{lesson_id}"),
                InlineKeyboardButton(text="❓ Подсказка", callback_data=f"hint_{lesson_id}")
            ],
            [
                InlineKeyboardButton(text="⏸️ Пауза", callback_data="pause"),
                InlineKeyboardButton(text="🚪 Выйти", callback_data="exit_lesson")
            ],
            [
                InlineKeyboardButton(text="🌐 Открыть в браузере", url=WEBAPP_URL)
            ]
        ]
    )
    return keyboard

def get_callback_data():
    """Callback data для обработки нажатий"""
    return {
        'start_lesson': 'start_lesson',
        'next_question': 'next_question',
        'check_answer': 'check_answer',
        'show_hint': 'show_hint',
        'exit_lesson': 'exit_lesson'
    }
