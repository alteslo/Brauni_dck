from peewee import *


db = SqliteDatabase(r"app\data\main.db")


class BaseModel(Model):
    class Meta:
        database = db


class Telegram_User(BaseModel):
    user_id = IntegerField(primary_key=True)
    name = CharField()
    birthday = CharField(null=True)
    ded = CharField(null=True)
    naval = CharField(null=True)

    class Meta:
        db_table = "users"


class User_Chat(BaseModel):
    user_id = IntegerField()
    chat_id = CharField()

    class Meta:
        db_table = "users_chats"


users = [user for user in Telegram_User.select()]
print(*users)

us_id = 777777777
# new_user = Telegram_User.create(user_id=us_id, name="Fil")
# new_chat = User_Chat.create(user_id=us_id, chat_id="-9999777")

print("Обработало идем Дальше\n\n")

users = [user for user in Telegram_User.select(Telegram_User)]
# chats = [chat for chat in User_Chat.select()]
print(*users)
