from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from database import get_category


async def get_category_keyboard():
    categories = await get_category()
    
    category_buttons = [
        [KeyboardButton(text=f"📚 {category['title']}")] for category in categories
    ]
    
    category_b = ReplyKeyboardMarkup(
        keyboard=category_buttons,
        resize_keyboard=True
    )
    return category_b

