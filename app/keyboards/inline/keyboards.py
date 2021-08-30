from aiogram import types


async def kb_interviwe(buttons=1, row_width=1):
    if buttons == 1:
        button = [types.InlineKeyboardButton(text="Пройдемте!",
                                            url="https://t.me/Brauni_dickbot",
                                            callback_data="interviwe")]
    else:
        button = [
            types.InlineKeyboardButton(text="Я спиздел!",
                                       url="https://t.me/Brauni_dickbot",
                                       callback_data="interviwe"),
            types.InlineKeyboardButton(text="Пошел нахуй",
                                       callback_data="interviwe")
                                       ]
    keyboard = types.InlineKeyboardMarkup(row_width=row_width)
    keyboard.add(*button)
    return keyboard
