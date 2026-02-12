import os
import sqlite3
from controller import *

class UserRepository:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        db_path = os.path.join(os.path.dirname(__file__), 'user_db.sqlite')
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, new_user):
        self.connect()
        self.cursor.execute(
        '''INSERT INTO users (user_id, username, password)
        values
            (?,?,?)''',
        [new_user.user_id, new_user.username, new_user.password]
        )
        self.disconnect(commit=True)