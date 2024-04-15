from aiogram import Router
from aiogram import F
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

router:Router = Router()

@router.message()
async def process_start_command(message: Message):
    await message.answer(
        text='Я вас не понимаю\n Выбираейте пункт меню. \n На посторонние вопросы не отвечаю.'
                         )