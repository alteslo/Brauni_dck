from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext, filters

import re

from app.utils.db_api.sqlite import db
from app.keyboards.inline import keyboards


async def interview(message: types.Message):

    keyboard = await keyboards.kb_private_in()
    await message.answer(text="Петушок.\nТеперь ответь на вопрос",
                         reply_markup=keyboard)


async def birthday(call: types.CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.answer(
        "Назови дату своего рождения в формате 'dd.mm.yyyy'")
    await state.set_state("wait_birthday")


async def check_stop(call: types.CallbackQuery):
    await call.answer()
    await call.message.edit_text("Сам иди нахуй!")


async def check_answer(message: types.Message, state: FSMContext):
    print(f"{message.text=}")
    msg_parse = re.compile(
        r"^(?:(?:31(\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\.)"
        r"(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\.)"
        r"0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|"
        r"(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\.)"
        r"(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$"
        )
    parsed = msg_parse.match(message.text)
    if parsed:
        print(f"{parsed=}")
        db.update_user_birthday(message.text, message.from_user.id)
        await message.answer("Записал")
        await state.finish()
    else:
        await message.answer("Ты читать не умеешь?\n"
                             "Ответ должен быть в формате 'dd.mm.yyyy'\n"
                             "Пробуй снова")


def register_handlers_interview(dp: Dispatcher):
    dp.register_callback_query_handler(check_stop,
                                       filters.ChatTypeFilter(
                                            types.ChatType.SUPERGROUP),
                                       text="stop")
    dp.register_message_handler(interview,
                                filters.ChatTypeFilter(
                                    types.ChatType.PRIVATE),
                                commands="start")
    dp.register_callback_query_handler(birthday,
                                       filters.ChatTypeFilter(
                                           types.ChatType.PRIVATE),
                                       text="interview")
    dp.register_message_handler(check_answer,
                                filters.ChatTypeFilter(
                                    types.ChatType.PRIVATE),
                                state="wait_birthday")
