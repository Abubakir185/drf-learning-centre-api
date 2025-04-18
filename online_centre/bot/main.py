from dispatcher import dp
from bot import bot 
import asyncio
from database import connect

async def on_start():
    print("bot has been started")

async def main():
    await connect()

    dp.startup.register(on_start)

    await dp.start_polling(bot)


asyncio.run(main()) 
