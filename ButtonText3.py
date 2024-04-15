from aiogram import Router
from aiogram import F
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

from text3 import *

router:Router = Router()


@router.message(F.text == 'Обнаружение сувенирных колюще режущих предметов')
async def process_start_command(message: Message):
    await message.answer(
        text=text_3_1,
        # удаление клавиатуры после ее нажатия
        reply_markup=ReplyKeyboardRemove()
                         )