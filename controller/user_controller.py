from model.entity.user_class import User
from model.repository.user_repository import UserRepository


class UserController:

    def save_user(self, username, password):
            user = User(username=username, password=password)
            user_repo = UserRepository()
            return user_repo.save_user(user)


