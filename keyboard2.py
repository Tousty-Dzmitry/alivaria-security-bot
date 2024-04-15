
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

button_2_1: KeyboardButton = KeyboardButton(text='Phone')
button_2_2: KeyboardButton = KeyboardButton(text='button-2')
button_3: KeyboardButton = KeyboardButton(text='button-3')
button_4: KeyboardButton = KeyboardButton(text='button-4')
button_5: KeyboardButton = KeyboardButton(text='button-5')
button_6: KeyboardButton = KeyboardButton(text='button-6')
button_7: KeyboardButton = KeyboardButton(text='button-7')
button_8: KeyboardButton = KeyboardButton(text='button-8')
button_9: KeyboardButton = KeyboardButton(text='button-9')

# Создаем объект клавиатуры, добавляя в него кнопки
keyboard_2: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                        keyboard=[[button_2_1], [button_2_2]])#, [button_3],
                                  # [button_4, button_5, button_6]#,
                                  # [button_7, button_8, button_9]])




