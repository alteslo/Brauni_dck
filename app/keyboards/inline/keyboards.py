from aiogram import types


async def kb_interviwe(buttons=1):
    if buttons == 1:
        button = [types.InlineKeyboardButton(text="Пройдемте!",
                                             url="https://t.me/Brauni_dickbot")]
    else:
        button = [
            types.InlineKeyboardButton(text="Я спиздел!",
                                       url="https://t.me/Brauni_dickbot"),
            types.InlineKeyboardButton(text="Пошел нахуй",
                                       callback_data="stop")
                                       ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*button)
    return keyboard


async def kb_private_in():
    button = types.InlineKeyboardButton(text="Валяй",
                                        callback_data="interview")
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button)
    return keyboard
