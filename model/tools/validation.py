import re

def id_validator(user_id):
    if not type(user_id) is int:
        raise TypeError('id must be an integer')


def username_validator(username):
    if not isinstance(username, str):
        raise TypeError("username must be a string")

    pattern = r'^[^@]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}$'

    if not re.match(pattern, username):
        raise ValueError("username must be a valid email address like: a@domain.com")


def password_validator(password):
    if not isinstance(password, str):
        raise TypeError("password must be a string")

    pattern = r'^(?=.*[A-Za-z])(?=.*\d).{6,}$'
    if not re.match(pattern, password):
        raise ValueError("password must be at least 6 characters, include at least one letter and one digit")
