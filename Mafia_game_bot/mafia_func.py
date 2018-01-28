from telebot import types
import random
"""

Клавиатуры для шагов игры.
Генератор случайных чисел для кода комнаты.

"""


def clean_keyboard():
    return types.ReplyKeyboardRemove()


def dialog_keyboard(key):
    if key == 1:
        first_dialog = types.ReplyKeyboardMarkup()
        first_dialog.row('Начать', 'Присоединиться')
        return first_dialog


def room_code():
    i = 0
    code = []
    while i <= 5:
        code.append(str(random.randint(0, 9)))
        i += 1
    return ''.join(code)

