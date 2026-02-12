import re

def id_validator(user_id):
    if not type(user_id) is int:
        raise TypeError('id must be an integer')

def username_validator(username):
    if not type(username) is str and re.match(r'^[^@]+@[^@\.]+\.[^@\.]+$', username):
        raise TypeError('username must be a valid email address like: a@domain.com')


def password_validator(password):
    if not type(password) is str and re.match(r'^(?=.*[A-Za-z])(?=.*\d).{6,}$' and password):
        raise TypeError('password must be a valid password at least 6 characters with one digit')

