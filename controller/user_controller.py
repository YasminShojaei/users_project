from model.entity import user_class
from model.entity.user_class import User
from model.repository import user_repository
from model.repository.user_repository import UserRepository


class UserController:

    def save_user(self, user_id, username, password):
        try:
            user = User(user_id, username, password)
            user_repo = UserRepository()
            user_repo.save(user)
            return True
        except Exception as e:
            return False, f"error is: {e}"

