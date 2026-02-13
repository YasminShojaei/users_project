from model.tools import validation
from model.tools.validation import id_validator, username_validator, password_validator


class User:
    def __init__(self, username, password, user_id=None):
        self.user_id = user_id
        self.username = username
        self.password = password


    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        id_validator(value)
        self._user_id = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        username_validator(value)
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        password_validator(value)
        self._password = value




