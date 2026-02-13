import sqlite3

from model.entity.user_class import User
from model.repository.db_config import DB_PATH

class UserRepository:

    def save_user(self, user:User):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users ( username, password) VALUES ( ?, ?)",
                (user.username, user.password)
            )
            return cursor.lastrowid
