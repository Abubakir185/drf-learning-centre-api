from aiogram import Dispatcher, F
from aiogram.filters import Command
from handler import start_handler, on_category_handler, on_course_handler, ortga_handler, ortga_handler_lesson

dp = Dispatcher()

dp.message.register(start_handler, Command("start"))
dp.message.register(on_category_handler, F.text.startswith("📚"))
dp.message.register(on_course_handler, F.text.startswith("📖"))
dp.message.register(ortga_handler, F.text == ("🔙 Kategoriyalarga"))
dp.message.register(ortga_handler_lesson, F.text == ("🔙 Orqaga"))