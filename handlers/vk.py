from aiogram import types
from loader import dp
from utils.misc.vk_password_change import VK


@dp.message_handler(content_types=types.ContentType.TEXT)
async def vk_auth(message: types.Message):
    try:
        username, password = message.text.split(":")
    except ValueError:
        await message.answer("Неверный формат данных. Повторите попытку")
        return

    response = VK()
    new_password = await response.password_change(username, password)
    if new_password:
        await message.answer(f"{username}:{new_password}")
    else:
        await message.answer(f"Не удалось сменить пароль от аккаунта:\n{username}:{password}")
