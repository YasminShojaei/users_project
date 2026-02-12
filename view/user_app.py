from controller import user_controller


def save_user(self):
    user_id = self.user_id.get()
    username = self.username.get()
    password = self.password.get()

    u_controller = UserController()
    result = u_controller.save_user(user_id, username, password)
    if result:
        print('User saved')

