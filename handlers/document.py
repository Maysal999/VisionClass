import os

from aiogram import Router
from aiogram.types import Message
from aiogram import Bot

from utils import translate_func

document_router = Router()


@document_router.message(lambda message: message.document)
async def handle_document(message: Message, bot: Bot):
    document = message.document
    file = await bot.get_file(document.file_id)
    file_path = f'files/{document.file_name}'
    # Скачиваем документ (BytesIO объект)
    file = await bot.download(document,file_path) 
    response = "\n".join(translate_func(file_path))
    if len(response) > 4096:
        # Отправляем сообщение частями, если оно слишком большое
        for i in range(0, len(response), 4096):
            await message.answer(response[i : i + 4096])
            await os.remove(file_path)
    else:
        await message.answer(response)
        await os.remove(file_path)
     # Читаем и декодируем содержимое файла в строку
    # try:
    #     with open(file_path, "r", encoding="utf-8") as file:
    #         content = file.read()
    #         await message.answer(f"Содержимое файла:\n{content[:200]}")  # Показать первые 200 символов
    # except Exception as e:
    #     await message.answer(f"Не удалось прочитать файл: {e}")
    