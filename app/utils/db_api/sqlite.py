import sqlite3
import datetime


class Database():
    """Модель базы данных"""
    def __init__(self, path_to_db=r"app\data\main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None,
                fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()

        connection = self.connection
        cursor = connection.cursor()
        cursor.execute(sql, parameters)
        data = None

        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()

        connection.close()
        return data

    def create_table_users(self):
        """Создаем структуру базы данных"""
        sql = """
        CREATE TABLE users(
            user_id INT PRIMARY KEY NOT NULL,
            name VARCHAR(150) NOT NULL,
            birthday VARCHAR(150),
            ded VARCHAR(150),
            naval VARCHAR(150));
        """
        self.execute(sql, commit=True)

    def create_table_users_chats(self):
        """Создаем структуру базы данных"""
        sql = """
        CREATE TABLE users_chats(
            user_id INT,
            chat_id VARCHAR(150));
        """
        self.execute(sql, commit=True)

    def add_user(self, user_id: int, name: str, birthday: str = None, ded: str = None, naval: str = None, chat_id: str = None):
        """Добавляем нового пользователя"""
        sql = """INSERT INTO users(user_id, name, birthday, ded, naval) VALUES (?, ?, ?, ?, ?);
                 INSERT INTO users_chats(user_id, chat_id) VALUES (?, ?);"""
        parameters = (user_id, name, birthday, ded, naval, chat_id)
        self.execute(sql, parameters=parameters, commit=True)

    def select_all_users(self):
        """Возвращает всех пользователей"""
        sql = """SELECT * FROM users"""
        return self.execute(sql, fetchall=True)

    def select_id_users(self):
        """Возвращает id всех пользователей"""
        sql = """SELECT user_id FROM users;"""
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        """Метод используемый как функция с помощью @staticmethod"""
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name=?"
        sql += " AND ".join([f'{item} = ?' for item in parameters])
        return sql, tuple(parameters.values())

    def select_user(self, **kwargs):
        """Возвращает пользователя"""
        sql = """SELECT * FROM users WHERE """
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        """Возвращает количесво пользователей"""
        sql = """SELECT COUNT(*) FROM users"""
        return self.execute(sql, fetchone=True)

    def update_user_birthday(self, birthday, user_id):
        sql = """UPDATE users SET birthday=? WHERE user_id=?"""
        return self.execute(sql, parameters=(birthday, user_id), commit=True)

    def update_user_ded(self, ded, user_id):
        sql = """UPDATE users SET ded=? WHERE user_id=?"""
        return self.execute(sql, parameters=(ded, user_id), commit=True)

    def update_user_naval(self, naval, user_id):
        sql = """UPDATE users SET naval=? WHERE user_id=?"""
        return self.execute(sql, parameters=(naval, user_id), commit=True)

    def update_chat_id(self, chat_id, user_id):
        sql = """UPDATE users SET chat_id=? WHERE user_id=?"""
        return self.execute(sql, parameters=(chat_id, user_id), commit=True)

    def select_chat_id(self, user_id):
        sql = """SELECT chat_id FROM users WHERE user_id=?"""
        return self.execute(sql, parameters=(user_id,), fetchone=True)

    def delete_users(self):
        sql = """DELETE FROM users"""
        self.execute(sql, commit=True)


db = Database()

# db.delete_users()
