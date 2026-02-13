from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from controller.user_controller import UserController
from model.repository.database_creator import create_database

class MainProgram:
    def __init__(self):
        pass
        self.user_controller = UserController()

    def menu(self):

        while True:
            print("\n_____________________")
            print("Welcome to User App")
            print("1. Enter user data")
            print("2. Exit")
            print("_____________________")

            user_input = input("Select an option: ").strip()

            if user_input == "1":
                self.enter_database()
            elif user_input == "2":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose 1 or 2.")

    def enter_database(self):

        print("\nEnter user information:")

        username = input("Username (email): ").strip()
        password = input("Password: ").strip()

        result = self.user_controller.save_user(username, password)
        print(f"User saved successfully with ID: {result}")

        if result:
            print("User saved successfully.")
        elif isinstance(result, tuple) and len(result) == 1:
            print(result[0])
        else:
            print("User could not be saved.")


if __name__ == "__main__":
    create_database()
    app = MainProgram()
    app.menu()

