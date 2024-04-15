from aiogram import Router
from aiogram import F
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

from text import *
router:Router = Router()

@router.message(F.text == 'Цель')
async def process_start_command(message: Message):
    await message.answer(
        text=text_1,
        # удаление клавиатуры после ее нажатия
        reply_markup=ReplyKeyboardRemove()
                         )


@router.message(F.text == 'Область применения')
async def process_start_command(message: Message):
    await message.answer(
        text=text_2,
        # удаление клавиатуры после ее нажатия
        reply_markup=ReplyKeyboardRemove()
                         )

@router.message(F.text == 'Термины, сокращения и обозначения')
async def process_start_command(message: Message):
    await message.answer(
        text=text_3,
        # удаление клавиатуры после ее нажатия
        reply_markup=ReplyKeyboardRemove()
                         )


@router.message(F.text == 'Ответственность')
async def process_start_command(message: Message):
    await message.answer(
        text=text_4,
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text == 'Нормативные ссылки')
async def process_start_command(message: Message):
    await message.answer(
        text=text_5,
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text == 'Предоставление доступа - общие положения')
async def process_start_command(message: Message):
    await message.answer(
        text=text_6,
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text == 'Досмотр')
async def process_start_command(message: Message):
    await message.answer(
        text=text_7,
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text == 'Предоставление доступа работникам Компании')
async def process_start_command(message: Message):
    await message.answer(
        text=text_8,
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text == 'Предоставление доступа арендаторам')
async def process_start_command(message: Message):
    await message.answer(
        text=text_9,
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text == 'Предоставление доступа подрядчикам')
async def process_start_command(message: Message):
    await message.answer(
        text=text_10,
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text == 'Предоставление доступа посетителям')
async def process_start_command(message: Message):
    await message.answer(
        text=text_11,
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text == 'Предоставление доступа транспортным средствам и водителям')
async def process_start_command(message: Message):
    await message.answer(
        text=text_12,
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text == 'Контроль доступа и пребывания')
async def process_start_command(message: Message):
    await message.answer(
        text=text_13,
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text == 'Порядок и условия проведения личного досмотра. Часть 1')
async def process_start_command(message: Message):
    await message.answer(
        text=text_14_1,
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text == 'Порядок и условия проведения личного досмотра. Часть 2')
async def process_start_command(message: Message):
    await message.answer(
        text=text_14_2,
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(F.text == 'Порядок и условия проведения досмотра вещей')
async def process_start_command(message: Message):
    await message.answer(
        text=text_15,
        # удаление клавиатуры после ее нажатия
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text == 'Порядок и условия проведения досмотра документов')
async def process_start_command(message: Message):
    await message.answer(
        text=text_16,
        # удаление клавиатуры после ее нажатия
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text == 'Порядок и условия проведения досмотра транспортных средств. Часть 1')
async def process_start_command(message: Message):
    await message.answer(
        text=text_17_1,
        # удаление клавиатуры после ее нажатия
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text == 'Порядок и условия проведения досмотра транспортных средств. Часть 2')
async def process_start_command(message: Message):
    await message.answer(
        text=text_17_2,
        # удаление клавиатуры после ее нажатия
        reply_markup=ReplyKeyboardRemove()
    )



@router.message(F.text == 'Порядок действий при обнаружении подозрительных предметов')
async def process_start_command(message: Message):
    await message.answer(
        text=text_18,
        # удаление клавиатуры после ее нажатия
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text == 'Должностная инструкция. Общие положения.')
async def process_start_command(message: Message):
    await message.answer(
        text=text_2_1,
        # удаление клавиатуры после ее нажатия
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(F.text == 'Должностная инструкция. Должностные обязанности. Часть 1')
async def process_start_command(message: Message):
    await message.answer(
        text=text_2_2_1,
        # удаление клавиатуры после ее нажатия
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text == 'Должностная инструкция. Должностные обязанности. Часть 2')
async def process_start_command(message: Message):
    await message.answer(
        text=text_2_2_2,
        # удаление клавиатуры после ее нажатия
        reply_markup=ReplyKeyboardRemove()
    )



@router.message(F.text == 'Должностная инструкция. Права.')
async def process_start_command(message: Message):
    await message.answer(
        text=text_2_3,
        # удаление клавиатуры после ее нажатия
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text == 'Должностная инструкция. Ответственность.')
async def process_start_command(message: Message):
    await message.answer(
        text=text_2_4,
        # удаление клавиатуры после ее нажатия
        reply_markup=ReplyKeyboardRemove()
    )

