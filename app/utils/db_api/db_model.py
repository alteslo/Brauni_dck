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
    user_id = ForeignKeyField(Telegram_User)
    chat_id = CharField()

    class Meta:
        db_table = "users_chats"
        primary_key = False


class Databse():
    def __init__(self):
        pass

    def create_table_users(self):
        pass

    def select_all_user(self):
        """Возвращает всех пользователей"""
        query = Telegram_User.select()
        users_information = []
        for i in query:
            users_information.append((i.user_id, i.name, i.birthday, i.ded, i.naval))
        return users_information

    def select_all_users_id(self):
        """Возвращает все id пользователей"""
        query = Telegram_User.select()
        users_id = [i.user_id for i in query]
        return users_id

    def select_user(self, user_id):
        """Возвращает данные пользователя"""
        query = User_Chat.select().where(User_Chat.user_id == user_id)
        users_id = [i.chat_id for i in query]
        query = Telegram_User.select().where(Telegram_User.user_id == user_id)
        user_inf = []
        for i in query:
            user_inf.extend([i.user_id, i.name, i.birthday, i.ded, i.naval])
        user_inf.append(users_id)
        return user_inf

    def select_current_chat_users(self, chat_id):
        """Возвращает все user_id для указанного чата"""
        query = Telegram_User.select().join(User_Chat).where(User_Chat.chat_id == chat_id)
        current_chat_users_id = [i.user_id for i in query]
        return current_chat_users_id

    def select_chats_user_in(self, user_id):
        """Возвращает список чатов доступных для пользователя"""
        query = User_Chat.select().where(User_Chat.user_id == user_id)
        users_id = [i.chat_id for i in query]
        return users_id

    def add_user(self, user_id: int, chat_id: str, name: str, birthday: str = None, ded: str = None, naval: str = None):
        Telegram_User.create(
            user_id=user_id,
            name=name,
            birthday=birthday,
            ded=ded,
            naval=naval)
        User_Chat.create(user_id=user_id, chat_id=chat_id)

    def add_user_in_user_chat(self, user_id: int, chat_id: str):
        User_Chat.create(user_id=user_id, chat_id=chat_id)

    def update_user(self):
        User_Chat

    def delete_users(self):
        pass


a = Databse()
# a.add_user(user_id=11111, chat_id="-222222", name="Victor")
b = a.select_user(610843180)
print(b[-1])
