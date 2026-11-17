
import unittest
import tempfile
import sqlite3
from pathlib import Path
from unittest.mock import patch

from secure_app import database
from secure_app.security import hash_password


class TestApplication(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

        self.db_path = Path(self.temp_dir.name) / "test.db"

        self.database_patch = patch.object(
            database, "DATABASE", self.db_path
        )

        self.database_patch.start()

        database.initialize_database()

    def tearDown(self):
        self.database_patch.stop()
        self.temp_dir.cleanup()

    def test_user_registration(self):
        result = database.create_user(
            "student123",
            hash_password("TestPass123!")
        )

        self.assertTrue(result)

    def test_duplicate_username(self):
        password_hash = hash_password("TestPass123!")

        database.create_user("student123", password_hash)

        result = database.create_user(
            "student123",
            password_hash
        )

        self.assertFalse(result)

    def test_user_login_lookup(self):
        password_hash = hash_password("TestPass123!")

        database.create_user("student123", password_hash)

        user = database.get_user("student123")

        self.assertIsNotNone(user)

    def test_sql_injection_protection(self):
        database.create_user(
            "student123",
            hash_password("TestPass123!")
        )

        malicious_username = "' OR '1'='1"

        user = database.get_user(malicious_username)

        self.assertIsNone(user)

    def test_add_student(self):
        database.add_student(
            "Logendra",
            "logendra@gmail.com",
            19
        )

        students = database.get_students()

        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]["name"], "Logendra")

    def test_duplicate_student_email(self):
        database.add_student(
            "Logendra",
            "logendra@gmail.com",
            19
        )

        with self.assertRaises(sqlite3.IntegrityError):
            database.add_student(
                "Another Student",
                "logendra@gmail.com",
                20
            )


if __name__ == "__main__":
    unittest.main()
