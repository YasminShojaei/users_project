from model.entity import user_class
from model.entity.user_class import User
from model.repository import user_repository
from model.repository.user_repository import UserRepository


class UserController:

    def save_user(self, username, password):
            user = User(username=username, password=password)
            user_repo = UserRepository()
            return user_repo.save_user(user)


