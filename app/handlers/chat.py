from aiogram import Dispatcher, types
from aiogram.dispatcher import filters

import re
import random

from aiogram.types.user import User
from aiogram.utils.mixins import T

from app.utils.db_api.sqlite import db


async def brauni_invoice(message: types.Message):
    msg_parse = re.compile(r"^([б|Б][р|Р][а|А][у|У][н|Н][и|И],?\s?[к|К][Т|т][о|О])\s?(.*)")
    parsed = msg_parse.match(message.text)
    if parsed:
        rofl_question = parsed.group(2).replace("?", "!")

        rofl_users = {user[0]: user[1] for user in db.select_all_users()}
        rofl_users_id = [user_id for user_id in rofl_users]

        user_id = random.choice(rofl_users_id)

        user_link = f"tg://user?id={user_id}"
        user_name = f"@{rofl_users.get(user_id)}"
        await message.reply(text=f"<a href='{user_link}'>{user_name}</a> {rofl_question}",parse_mode="HTML")
    else:
        await message.reply("Хуяуни, я тебе не ИИ всратый, отвечу только на вопрос кто")


def register_handlers_regex(dp: Dispatcher):
    dp.register_message_handler(brauni_invoice,
                                filters.Text(
                                    startswith="брауни", ignore_case=True),
                                filters.ChatTypeFilter(
                                    types.ChatType.SUPERGROUP)
                                )
