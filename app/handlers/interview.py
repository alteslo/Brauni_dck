from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext, filters

from app.keyboards.inline import keyboards


async def msg_in_priv_chat(call: types.CallbackQuery):
    print("WELCOME")
    button = types.KeyboardButton("/start")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button)
    await call.bot.send_message(chat_id=call.from_user.id,
                                text=f"Приветствую {call.from_user.full_name}!",
                                reply_markup=keyboard)


async def interview(message: types.Message):

    keyboard = await keyboards.kb_private_in()
    await message.edit_text(text="Салага", reply_markup=types.ReplyKeyboardRemove)
    await message.answer(text="Теперь ответь на вопрос", reply_markup=keyboard)


async def birthday(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Назови дату своего рождения в формате 'dd.mm.yyyy'")
    await state.set_state("wait_birthday")


def register_handlers_interview(dp: Dispatcher):
    dp.register_callback_query_handler(msg_in_priv_chat, text="send_priv_msg")
    dp.register_message_handler(interview,
                                filters.ChatTypeFilter(
                                    types.ChatType.PRIVATE),
                                commands="start")
    dp.register_callback_query_handler(birthday,
                                       filters.ChatTypeFilter(
                                           types.ChatType.PRIVATE),
                                       text="interview")
