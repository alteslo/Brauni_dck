from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command

import random
import re


async def byba(message: types.Message):
    """Измеряет твою бибу или бибу друга"""
    command_parse = re.compile(r"(!biba|/biba) ?([\w+ ]+)?")
    parsed = command_parse.match(message.text)
    target = parsed.group(2)
    length = random.randint(3, 25)

    if message.reply_to_message:
        target = message.reply_to_message.from_user.get_mention(as_html=True)
    else:
        target = message.from_user.get_mention(as_html=True)

    await message.reply(f"У {target} биба {length} см", parse_mode='HTML')


async def gay(message: types.Message):
    """Измеряет уровень гомосексуализма"""
    pass


def register_handlers_rofl(dp: Dispatcher):
    """Регистрируем рофляные хэндлеры"""
    dp.register_message_handler(byba, Command(commands="biba", prefixes='!/'))
    dp.register_message_handler(gay, Command(commands="gay", prefixes='!/'))
