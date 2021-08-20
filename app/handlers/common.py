from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
import sqlite3

from app import keyboards
from app.states.interview import Interview
from app.utils.db_api.sqlite import db


async def interview_start(message: types.Message):
    """Обработчик первого шага, реагирующий на команду start"""

    await message.answer(f"Привет {message.from_user.get_mention(as_html=True)}")
    """
    await state.finish()
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_fname = message.from_user.full_name

    try:
        db.add_user(user_id, user_fname)
    except sqlite3.IntegrityError as err:
        print("___________________________________________")
        print(err)

    await message.answer(text=f"Приветствую, {user_name}!",
                         reply_markup=types.ReplyKeyboardRemove())
    keyboard = await keyboards.kb_service_selection()
    await message.answer(text="Какую услугу вы хотите получить?",
                         reply_markup=keyboard)

    await Interview.waiting_for_service_selection.set()"""


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(interview_start, commands="start")
