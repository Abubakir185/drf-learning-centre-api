from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bot import bot
from buttons import get_category_keyboard
from database import get_category, get_courses_id, get_courses

async def start_handler(msg: Message):
        category = await get_category_keyboard()
        await msg.answer(f"Assalomu alaykum {msg.from_user.full_name}, botga hush kelibsiz!", reply_markup=category)

async def on_category_handler(message: Message):
    user_category = message.text[2:]
    categories = await get_category()
    
    category_id = None
    for c in categories:
        if user_category == c['title']:
            category_id = c['cat_id']
            break
    
    if category_id is None:
        await message.answer("Bunday kategoriya mavjud emas. Iltimos, boshqa kategoriya tanlang.")
        return

    await message.answer(f"Tanlangan kategoriya: {user_category}")


    courses = await get_courses_id(category_id)
    course_buttons = []
    for course in courses:
        course_buttons.append([KeyboardButton(text=f"📖 {course['title']}")]) 
        course_buttons.append([KeyboardButton(text="🔙 Orqaga")])
    courses_b = ReplyKeyboardMarkup(keyboard=course_buttons, resize_keyboard=True)

    await message.answer("Tanlangan kategoriya bo'yicha kurslar:", reply_markup=courses_b)


async def on_course_handler(message: Message):
    user_course = message.text[2:]
    course = await get_courses()

    course_id = None
    for c in course:
        if user_course == c['title']:
            course_id = c['id']
            break

    if course_id is None:
        await message.answer("Bunday kurs mavjud emas. Iltimos, boshqa kurs tanlang.")
        return
   
    await message.answer(f"Tanlangan kurs: {user_course}")

    caption = (
        "🎓 <b>Kurs haqida ma'lumot:</b>\n"
        f"📌 <b>Nomi:</b> {c['title']}\n"
        f"📝 <b>Ma'lumot:</b> {c['description']}\n\n"
        f"💰 <b>Kurs narxi:</b> {c['price']} so'm"
    )

    await bot.send_photo(message.chat.id, c['image'], caption=caption, parse_mode="HTML")

async def ortga_handler(message: Message):
    category = await get_category_keyboard()
    await message.answer("Ortga qaytish", reply_markup=category)