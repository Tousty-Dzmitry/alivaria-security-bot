from aiogram import Router
from aiogram import F
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

from aiogram.types import FSInputFile


from text2 import *
router:Router = Router()

@router.message(F.text == 'Phone')
async def process_start_command(message: Message):
    await message.answer(
        text=Phone_Number,
        # удаление клавиатуры после ее нажатия
        reply_markup=ReplyKeyboardRemove()
                         )
# @router.message(F.text == 'Схема территории завода')
# async def process_start_command(message: Message):
#     await message.answer(
#         await bot.send_photo(message.chat.id, photo, reply_to_message_id=message.message_id),
#         # удаление клавиатуры после ее нажатия
#         reply_markup=ReplyKeyboardRemove()
#                         )

