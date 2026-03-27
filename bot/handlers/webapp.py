from aiogram import Router, types
import json
import logging

router = Router()
logger = logging.getLogger(__name__)

# Ваш WebApp URL
WEBAPP_URL = "https://morion123.github.io/Egelingo1"
# Ваш API токен
BOT_TOKEN = "8771751592:AAHVJR4xjomMF3eXwjVbjcpqmClT-qA_KSk"

@router.message(lambda message: message.web_app_data is not None)
async def handle_webapp_data(message: types.Message):
    """Обработка данных из WebApp"""
    try:
        data = json.loads(message.web_app_data.data)
        action = data.get('action')
        user_id = message.from_user.id
        
        logger.info(f"Получены данные от пользователя {user_id}: {action}")
        
        if action == 'complete_lesson':
            lesson_id = data.get('lesson_id')
            score = data.get('score')
            subject = data.get('subject', 'unknown')
            
            # Расчет опыта
            xp_earned = int(score / 10)
            
            await message.answer(
                f"✅ <b>Урок успешно завершен!</b>\n\n"
                f"📚 Предмет: {subject}\n"
                f"📖 Урок #{lesson_id}\n"
                f"📊 Результат: {score}%\n"
                f"⭐️ Получено опыта: +{xp_earned} XP\n\n"
                f"🌐 Продолжить обучение: {WEBAPP_URL}\n\n"
                f"🎉 Отличная работа! Продолжайте в том же духе!",
                parse_mode="HTML"
            )
            
        elif action == 'get_stats':
            # Здесь будет запрос к базе данных
            stats = {
                'level': 5,
                'points': 1250,
                'streak': 7,
                'lessons_completed': 42,
                'accuracy': 87,
                'webapp_url': WEBAPP_URL
            }
            
            await message.answer(
                json.dumps(stats)
            )
            
        elif action == 'save_progress':
            subject = data.get('subject')
            lesson_id = data.get('lesson_id')
            progress = data.get('progress')
            
            await message.answer(
                f"💾 <b>Прогресс сохранен!</b>\n\n"
                f"📚 Предмет: {subject}\n"
                f"📖 Урок: {lesson_id}\n"
                f"📊 Прогресс: {progress}%\n\n"
                f"🌐 {WEBAPP_URL}\n\n"
                f"Продолжайте обучение! 🚀",
                parse_mode="HTML"
            )
            
        elif action == 'get_leaderboard':
            # Тестовые данные рейтинга
            leaderboard = [
                {"name": "Иван", "points": 2500, "level": 8},
                {"name": "Мария", "points": 2100, "level": 7},
                {"name": "Алексей", "points": 1850, "level": 6},
                {"name": message.from_user.first_name, "points": 1250, "level": 5}
            ]
            
            await message.answer(
                json.dumps(leaderboard)
            )
            
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка парсинга JSON: {e}")
        await message.answer("❌ Произошла ошибка при обработке данных")
    except Exception as e:
        logger.error(f"Неизвестная ошибка: {e}")
        await message.answer("❌ Произошла непредвиденная ошибка")
