from itertools import chain
from aiogram import Dispatcher, types
from aiogram.dispatcher import filters

from app.utils.db_api.db_model import Databse
from app.keyboards.inline import keyboards


async def interview_start(message: types.Message):
    """Обработчик первого шага, реагирующий на команду start"""
    db = Databse()
    user_id = message.from_user.id
    chat_id = message.chat.id
    name = message.from_user.full_name
    db.select_current_chat_users(chat_id)
    
    print(message.chat.id)
    text = (f"Привет {message.from_user.get_mention(as_html=True)}!"
            f"\nТоварищ полковник интересуется тобой и придется ответить "
            f"на некоторые  вопросы.")

    db_user = db.select_user(user_id=user_id, chat_id=message.chat.id)
    if db_user:
        await message.answer(
            text="Ты уже взят на карандаш",
            reply_markup=await keyboards.kb_interviwe(buttons=2))
        await message.bot.send_message(
            chat_id=user_id,
            text=(f"По твоим словам ты родился {db_user[2]}, если не так - "
                  f"жми\n<b>/start</b>"),
            parse_mode="HTML")
    else:
        db.add_user(user_id=user_id, name=name, chat_id=message.chat.id)

        await message.answer(text=text, parse_mode='HTML',
                             reply_markup=await keyboards.kb_interviwe())
        await message.bot.send_message(
            chat_id=user_id,
            text="Нажми /start, чтобы пройти регистрацию")


async def help_info(message: types.Message):
    """Инструкция по командам"""
    user = message.from_user.full_name
    text = (f"Итак голубец, сейчас расскажу что к чему: \nнажми /start, чтобы зарегистрироваться"
            f"\nесть команда /gay \nесть команда /biba, узнай на сколько ты "
            f"гей и размер твоего члена, а если в ответе на чужое сообщение "
            f"ты укажешь эти команды, то ты узнаешь все про него &#129327;\n"
            f"А еще ты можешь задать мне вопрос 'Брауни, кто ...', придумай свой вопрос &#128520"
            f"\nЖми {user} на что хочешь &#9891;")

    await message.answer(text=text, parse_mode='HTML')


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(interview_start,
                                filters.ChatTypeFilter(
                                    types.ChatType.SUPERGROUP),
                                commands="start")
    dp.register_message_handler(help_info, commands="help")
