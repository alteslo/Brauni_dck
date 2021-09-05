from aiogram.utils.callback_data import CallbackData

interview_callback = CallbackData("interview", "user_id", "chat_id")

support_callback = CallbackData("ask_support", "messages", "user_id", "as_user")
cancel_support_callback = CallbackData("cancel_support", "user_id")
