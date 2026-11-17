
import sqlite3
from pathlib import Path
from contextlib import contextmanager

DATABASE = Path(__file__).resolve().parent / "students.db"


@contextmanager
def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row

    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash BLOB NOT NULL
            )
        """)

        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTEGER NOT NULL
            )
        """)


def create_user(username, password_hash):
    try:
        with get_connection() as connection:
            connection.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, password_hash)
            )
        return True
    except sqlite3.IntegrityError:
        return False


def get_user(username):
    with get_connection() as connection:
        return connection.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()


def add_student(name, email, age):
    with get_connection() as connection:
        connection.execute(
            "INSERT INTO students (name, email, age) VALUES (?, ?, ?)",
            (name, email, age)
        )
    return True


def get_students():
    with get_connection() as connection:
        return connection.execute(
            "SELECT id, name, email, age FROM students"
        ).fetchall()
