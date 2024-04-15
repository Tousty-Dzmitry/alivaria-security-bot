from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

#клавиатуру нужно сделать отдельным модулем

button_1: KeyboardButton = KeyboardButton(text='Цель')
button_2: KeyboardButton = KeyboardButton(text='Область применения')
button_3: KeyboardButton = KeyboardButton(text='Термины, сокращения и обозначения')
button_4: KeyboardButton = KeyboardButton(text='Ответственность')
button_5: KeyboardButton = KeyboardButton(text='Нормативные ссылки')
button_6: KeyboardButton = KeyboardButton(text='Предоставление доступа - общие положения')
button_7: KeyboardButton = KeyboardButton(text='Досмотр')
button_8: KeyboardButton = KeyboardButton(text='Предоставление доступа работникам Компании')
button_9: KeyboardButton = KeyboardButton(text='Предоставление доступа арендаторам')
button_10: KeyboardButton = KeyboardButton(text='Предоставление доступа подрядчикам')
button_11: KeyboardButton = KeyboardButton(text='Предоставление доступа посетителям')
button_12: KeyboardButton = KeyboardButton(text='Предоставление доступа транспортным средствам и водителям')
button_13: KeyboardButton = KeyboardButton(text='Контроль доступа и пребывания')
button_14_1: KeyboardButton = KeyboardButton(text='Порядок и условия проведения личного досмотра. Часть 1')
button_14_2: KeyboardButton = KeyboardButton(text='Порядок и условия проведения личного досмотра. Часть 2')
button_15: KeyboardButton = KeyboardButton(text='Порядок и условия проведения досмотра вещей')
button_16: KeyboardButton = KeyboardButton(text='Порядок и условия проведения досмотра документов')
button_17_1: KeyboardButton = KeyboardButton(text='Порядок и условия проведения досмотра транспортных средств. Часть 1')
button_17_2: KeyboardButton = KeyboardButton(text='Порядок и условия проведения досмотра транспортных средств. Часть 2')
button_18: KeyboardButton = KeyboardButton(text='Порядок действий при обнаружении подозрительных предметов')
button_19: KeyboardButton = KeyboardButton(text='Должностная инструкция. Общие положения.')
button_20_1: KeyboardButton = KeyboardButton(text='Должностная инструкция. Должностные обязанности. Часть 1')
button_20_2: KeyboardButton = KeyboardButton(text='Должностная инструкция. Должностные обязанности. Часть 2')
button_21: KeyboardButton = KeyboardButton(text='Должностная инструкция. Права.')
button_22: KeyboardButton = KeyboardButton(text='Должностная инструкция. Ответственность.')


# Создаем объект клавиатуры, добавляя в него кнопки
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                        keyboard=[[button_1], [button_2], [button_3], [button_4], [button_5],
                                  [button_6], [button_7], [button_8], [button_9], [button_10],
                                  [button_11], [button_12], [button_13], [button_14_1], [button_14_2],
                                  [button_15], [button_16], [button_17_1], [button_17_2], [button_18],
                                  [button_19], [button_20_1], [button_20_2], [button_21], [button_22]])



