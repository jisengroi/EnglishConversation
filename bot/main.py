import asyncio
from aiogram.client.default import DefaultBotProperties
from config.bot import BOT_TOKEN
from aiogram import Bot, Dispatcher, Router, types
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='w'  
)

router = Router()

@router.message()
async def echo(message: types.Message):
    await message.answer("Percobaan: English Conversation step 1")

async def main():
    # Inisialisasi bot dan dispatcher
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()

    # Mendaftarkan Router
    dp.include_router(router)

    # Mulai polling
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())