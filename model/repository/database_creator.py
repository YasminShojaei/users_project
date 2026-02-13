import sqlite3

def create_database():
    try:
        connection = sqlite3.connect('users_db.sqlite')
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        connection.commit()
        print("Database and table created")
    except Exception as e:
        print("Error:", e)
    finally:
        connection.close()
