
import unittest

from secure_app.security import hash_password, verify_password
from secure_app.validators import (
    validate_username,
    validate_password,
    validate_name,
    validate_email,
    validate_age
)


class TestSecurity(unittest.TestCase):

    def test_password_hashing(self):
        password = "TestPass123!"
        hashed = hash_password(password)

        self.assertNotEqual(hashed, password.encode())
        self.assertTrue(verify_password(password, hashed))

    def test_wrong_password(self):
        hashed = hash_password("TestPass123!")

        self.assertFalse(
            verify_password("WrongPass123!", hashed)
        )

    def test_username_validation(self):
        self.assertTrue(validate_username("student123"))
        self.assertFalse(validate_username("ab"))

    def test_password_validation(self):
        self.assertTrue(validate_password("TestPass123!"))
        self.assertFalse(validate_password("1234"))

    def test_name_validation(self):
        self.assertTrue(validate_name("Logendra"))
        self.assertFalse(validate_name("12345"))

    def test_email_validation(self):
        self.assertTrue(validate_email("student@gmail.com"))
        self.assertFalse(validate_email("invalid-email"))

    def test_age_validation(self):
        self.assertTrue(validate_age(19))
        self.assertFalse(validate_age(150))

    def test_sql_injection_input(self):
        malicious_input = "' OR '1'='1"
        self.assertFalse(validate_username(malicious_input))


if __name__ == "__main__":
    unittest.main()
