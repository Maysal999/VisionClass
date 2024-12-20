from aiogram import Router, F
from aiogram.types import Message

from utils import translate_text

text_router = Router()


@text_router.message(F.text)
async def text_handler(message: Message):
    try:
        text = message.text
        response = translate_text(text)
        if len(response) > 4096:
            for i in range(0, len(response), 4096):
                await message.answer(response[i : i + 4096])
        else:
            await message.answer(response)
    except Exception as e:
        await message.answer("Произошла ошибка при обработке текста. Попробуйте еще раз.")
        # Логируем ошибку (для разработчика)
        print(f"Ошибка: {e}")


