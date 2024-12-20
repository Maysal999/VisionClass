import asyncio

from aiogram import Dispatcher, Bot
from aiogram.filters import CommandStart,CommandObject
from aiogram.types import Message,BotCommand, ReplyKeyboardMarkup, KeyboardButton



from handlers import document_router, text_router, image_router


API_TOKEN = "7783270008:AAFHgtsh5IxYwxMYklXs4VPHMapJQluXQ_M"


bot = Bot(token=API_TOKEN)
dp = Dispatcher()

dp.include_routers(document_router,text_router,image_router)

@dp.message(CommandStart())
async def start_handler(message: Message ):
    await message.reply(
        "Привет! Я бот для перевода словарей. Отправьте мне файл .txt с английскими словами, и я переведу его на русский язык."
    )

@dp.message(CommandObject(prefix='/help'))
async def help_handler(message : Message):
    await message.answer(
        reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='contact',request_contact=True)]])
    )

async def main():
    await dp.start_polling(bot)
    # Устанавливаем команды (по желанию)
    await bot.set_my_commands([
        BotCommand(command="start", description="Начать"),
        BotCommand(command="help", description="Помощь"),
    ])


if __name__ == "__main__":
    asyncio.run(main())