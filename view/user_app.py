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
        pass



        print("\nEnter user information:")

        try:
            user_id = int(input("User ID (integer): ").strip())
        except ValueError:
            print("User ID must be an integer.")
            return

        username = input("Username (email): ").strip()
        password = input("Password: ").strip()

        result = self.user_controller.save_user(user_id, username, password)

        if result is True:
            print("User saved successfully.")
        elif isinstance(result, tuple) and len(result) == 2:
            print(result[1])
        else:
            print("User could not be saved.")


if __name__ == "__main__":
    create_database()
    app = MainProgram()
    app.menu()

import sqlite3
from model.repository.db_config import DB_PATH

with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    print("FINAL CHECK:", cursor.fetchall())
