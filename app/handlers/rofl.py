from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Command

import random
import re

from app.config_reader import load_config


async def byba(message: types.Message):
    """Измеряет твою бибу или бибу друга"""
    command_parse = re.compile(r"(!biba|/biba) ?([\w+ ]+)?")
    parsed = command_parse.match(message.text)
    rofl_user = parsed.group(2)
    length = random.randint(3, 25)

    config = load_config("config/bot.ini")
    terpila = config.tg_bot.terpila_id

    if message.reply_to_message:
        target = message.reply_to_message.from_user.get_mention(as_html=True)
    elif rofl_user:
        target = rofl_user
    else:
        target = message.from_user.get_mention(as_html=True)

    await message.reply(f"У {target} биба {length} см", parse_mode='HTML')


async def gay(message: types.Message):
    """Измеряет уровень гомосексуализма"""
    command_parse = re.compile(r"(!gay|/gay) ?([\w+ ]+)?")
    parsed = command_parse.match(message.text)
    rofl_user = parsed.group(2)
    percentage = random.randint(0, 100)

    if message.reply_to_message:
        target = message.reply_to_message.from_user.get_mention(as_html=True)
    elif rofl_user:
        target = rofl_user
    else:
        target = message.from_user.get_mention(as_html=True)

    await message.reply(f"Похоже {target} гей на {percentage}%", parse_mode='HTML')


def register_handlers_rofl(dp: Dispatcher):
    """Регистрируем рофляные хэндлеры"""
    dp.register_message_handler(byba, Command(commands="biba", prefixes='!/'))
    dp.register_message_handler(gay, Command(commands="gay", prefixes='!/'))
