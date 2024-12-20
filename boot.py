import logging
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from googletrans import Translator
from aiogram.types import FSInputFile

# Установите токен вашего Telegram-бота
API_TOKEN = "7783270008:AAFHgtsh5IxYwxMYklXs4VPHMapJQluXQ_M"

# Инициализация бота, диспетчера и переводчика
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
translator = Translator()

# Приветственное сообщение
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.reply(
        "Привет! Я бот для перевода словарей. Отправьте мне файл .txt с английскими словами, и я переведу его на русский язык."
    )

# Обработка текстовых файлов
@dp.message(lambda message: message.document)
async def handle_document(message: Message):
    file_name = message.document.file_name
    document = message.document
    await message.answer(f'Вы отправили документ: {type(document.file_name)}')
    # Проверяем, что файл имеет формат .txt
    if not file_name.endswith(".txt"):
        await message.reply("Пожалуйста, отправьте файл в формате .txt.")
        return

    # Скачиваем файл
    file_path = await bot.download(message.document)
    with open(file_path, "r", encoding="utf-8") as file:
        words = file.readlines()

    # Переводим слова
    translated_words = []
    for word in words:
        word = word.strip()  # Убираем лишние пробелы
        if word:
            translation = translator.translate(word, src="en", dest="ru").text
            translated_words.append(f"{word} - {translation}")

    # Создаем текстовый ответ
    response = "\n".join(translated_words)
    if len(response) > 4096:
        # Отправляем сообщение частями, если оно слишком большое
        for i in range(0, len(response), 4096):
            await message.answer(response[i : i + 4096])
    else:
        await message.answer(response)

# Обработка любых других сообщений
@dp.message()
async def fallback_message(message: Message):
    await message.reply("Пожалуйста, отправьте файл .txt с английскими словами для перевода.")

# Запуск бота
async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    
    asyncio.run(main())