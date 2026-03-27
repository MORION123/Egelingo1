from aiogram import Router, types
from aiogram.types import WebAppData
import json

router = Router()

@router.message(lambda message: message.web_app_data is not None)
async def handle_webapp_data(message: types.Message):
    """Обработка данных из WebApp"""
    data = json.loads(message.web_app_data.data)
    
    # Здесь логика сохранения результатов
    action = data.get('action')
    
    if action == 'complete_lesson':
        lesson_id = data.get('lesson_id')
        score = data.get('score')
        
        await message.answer(
            f"✅ Урок пройден!\n"
            f"Результат: {score}%\n"
            f"Получено очков: {score // 10}\n\n"
            f"Продолжайте в том же духе! 🎉"
        )
    
    elif action == 'get_stats':
        # Отправка статистики в WebApp
        await message.answer(
            json.dumps({
                'level': 5,
                'points': 1250,
                'streak': 7
            })
        )
