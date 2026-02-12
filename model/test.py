from model import *
from controller import *
from model.entity.user_class import User
from model.repository.user_repository import UserRepository

new_user = User(1, "yasmin@gmail.com", "yasmin1234")
user_repo = UserRepository()
user_repo.save(new_user)
print("User was added")