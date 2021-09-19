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
        query = Telegram_User.select()
        users_id = [i.user_id for i in query]
        return users_id

    def select_current_chat_users(self, chat_id):
        """Возвращает все user_id для указанного чата"""
        query = Telegram_User.select().join(User_Chat).where(User_Chat.chat_id == chat_id)
        current_chat_users_id = [i.user_id for i in query]
        return current_chat_users_id

    def select_chats_user_in(self, user_id):
        """Возвращает список чатов доступных для пользователя"""
        pass

    def add_user(self, user_id: int, chat_id: str, name: str, birthday: str = None, ded: str = None, naval: str = None):
        Telegram_User.create(
            user_id=user_id,
            name=name,
            birthday=birthday,
            ded=ded,
            naval=naval)
        User_Chat.create(user_id=user_id, chat_id=chat_id)

    def update_user(self):
        pass

    def delete_users(self):
        pass


a = Databse()
# a.add_user(user_id=11111, chat_id="-222222", name="Victor")
print(a.select_all_users_id())
