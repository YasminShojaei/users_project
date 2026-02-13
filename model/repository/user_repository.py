import sqlite3
from model.repository.db_config import DB_PATH

class UserRepository:

    def save_user(self, user):
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (user_id, username, password) VALUES (?, ?, ?)",
                (user.user_id, user.username, user.password)
            )
