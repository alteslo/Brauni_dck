from aiogram import Dispatcher, types

import sqlite3


from app.utils.db_api.sqlite import db


async def interview_start(message: types.Message):
    """Обработчик первого шага, реагирующий на команду start"""

    await message.answer(f"Привет {message.from_user.get_mention(as_html=True)}", parse_mode='HTML')


async def help_info(message: types.Message):
    """Инструкция по командам"""
    user = message.from_user.full_name
    text = f"Итак голубец, сейчас расскажу что к чему:\n есть команда /start\n \
есть команда /gay\n есть команда /biba жми {user} на что хочешь"

    await message.answer(text=text, parse_mode='HTML')


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(interview_start, commands="start")
    dp.register_message_handler(help_info, commands="help")
