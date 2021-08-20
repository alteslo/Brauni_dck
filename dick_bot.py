import telebot
import random
import os

ID_LEO = 792595229

token = os.environ["TOKEN"]
bot = telebot.TeleBot(token)


def pashalka(razmchlena):
    '''Пасхалка - возвращаем шуточную фразу на основе рандома '''
    rand = random.randrange(0, 10)
    if rand == 1:
        return f" спереди и {int(razmchlena * 10)} см сзади"
    else:
        return ""


@bot.message_handler(commands=['start'])
def start_msg(message):
    bot.reply_to(
        message, "Лео - царь гомосексуализма измеряет твой член. \
        Дай добро - напиши:"+"\n"+"/член"
        )


@bot.message_handler(commands=['член'])
def chlen_msg(message):
    if message.from_user.id == ID_LEO:
        # Рандом для Лео
        razmchlena = random.uniform(1, 3.5)
        user_name = message.from_user.first_name
        bot.reply_to(
            message, f"Царь Леонидас твой размер члена неизмерим\
            - примерно {round(razmchlena, 1)} сантиметра"
            + pashalka(razmchlena)
        )
    else:
        # Нормальный рандом
        razmchlena = random.uniform(1, 20)
        user_name = message.from_user.first_name
        # Для члена как у Лео
        if razmchlena <= 3.5:
            bot.reply_to(
                message, f"{user_name} твой член подобен царскому - \
                {round(razmchlena, 1)} сантиметра"
                + pashalka(razmchlena)
            )
        # Для нормального члена
        else:
            bot.reply_to(
                message, f"{user_name} твой размер члена - \
                {round(razmchlena, 1)} сантиметра"
                + pashalka(razmchlena)
            )


@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    user_name = message.new_chat_members[0].first_name
    bot.reply_to(message, f"Добро пожаловать, {user_name}")
    with open("chleny.txt", "a") as w:
        w.write(
            f"{message.new_chat_members[0].id}, \
            {message.new_chat_members[0].first_name}"+"\n"
            )


bot.polling()
