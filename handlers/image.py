import os



from aiogram import Router, F, Bot
from aiogram.types import Message


from utils import image_render

image_router = Router()



@image_router.message(F.photo)
async def text_handler(message: Message,bot: Bot):
    await message.reply('1234')
    image = message.photo[-1].file_id
    file_path = f'files/{image}'
    # Скачиваем документ (BytesIO объект)
    file = await bot.download(image, file_path)
    response = image_render(file_path)
    if len(response) > 4096:
            for i in range(0, len(response), 4096):
                await message.answer(response[i : i + 4096])
                await os.remove(file_path)

    else:
            await message.answer(response)
            await os.remove(file_path)