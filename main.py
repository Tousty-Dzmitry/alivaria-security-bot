# BOT_TOKEN = '6119057214:AAFfWbstixdSv64T34PMfUIDVcHSmKzEWJs'
# name in telegram= Сonstructor Bot
# id = 5489411423


from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

from lexicon import LEXICON_COMMANDS
from aiogram.types import BotCommand

from keyboard1 import keyboard
from keyboard2 import keyboard_2
from keyboard3 import keyboard_3
from text import *

from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User

#from aiogram import Bot, Dispatcher, F
#from aiogram.types import FSInputFile

import ButtonText1
import ButtonText2
import ButtonText3
import text4


from aiogram.types import FSInputFile
from aiogram.types import ReplyKeyboardRemove
# from text2 import photo
# import keyboard2
# from aiogram import Router


# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = '6119057214:AAFfWbstixdSv64T34PMfUIDVcHSmKzEWJs'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# @dp.message(Command(commands='delmenu'))
# async def del_main_menu(message: Message, bot: Bot):
#     await bot.delete_my_commands()
#     await message.answer(text='Кнопка "Menu" удалена')









# Функция для настройки кнопки Menu бота
async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in LEXICON_COMMANDS.items()
    ]
    await bot.set_my_commands(main_menu_commands)

# приватные пользователи

CACHE = {
    'private': [5489411423, '''784520574, Германов''', '''5524913683 русецкий'''],
}

# Middleware на допуск только приватных пользователей
class ShadowBanMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:

        user: User = data.get('event_from_user')
        if user is not None:
            if user.id in CACHE.get('private'):

                return await handler(event, data)


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Выбирайте в меню интересующий вас вопрос'
    )

@dp.message(Command(commands='command_1'))
async def process_start_command(message: Message):
    await message.answer(text='выбирайте нужную инструкцию',
                         reply_markup=keyboard)

@dp.message(Command(commands='command_2'))
async def process_start_command(message: Message):
    await message.answer(text='выбирайте нужный пункт',
                         reply_markup=keyboard_2)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@dp.message(Command(commands='command_3'))
async def process_start_command(message: Message):
    await message.answer(text='выбирайте вопрос',
                         reply_markup=keyboard_3)

@dp.message(Command(commands=['command_4']))
async def process_start_command(message: Message):
    photo_path = 'image/map.jpg'
    photo = FSInputFile(photo_path)
    await bot.send_photo(message.chat.id, photo, reply_to_message_id=message.message_id),
        # удаление клавиатуры после ее нажатия






dp.include_router(ButtonText1.router)
dp.include_router(ButtonText2.router)
dp.include_router(ButtonText3.router)
dp.include_router(text4.router)









if __name__ == '__main__':
    dp.update.middleware(ShadowBanMiddleware())

    dp.startup.register(set_main_menu)

    dp.run_polling(bot)

