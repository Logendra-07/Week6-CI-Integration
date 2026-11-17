
import re


def validate_username(username):
    if not isinstance(username, str):
        return False

    return bool(
        re.fullmatch(r"[a-zA-Z0-9_]{3,30}", username)
    )


def validate_password(password):
    if not isinstance(password, str):
        return False

    password_bytes = password.encode("utf-8")

    return (
        len(password_bytes) >= 8
        and len(password_bytes) <= 72
    )


def validate_name(name):
    if not isinstance(name, str):
        return False

    name = name.strip()

    return (
        2 <= len(name) <= 50
        and all(char.isalpha() or char.isspace() for char in name)
    )


def validate_email(email):
    if not isinstance(email, str):
        return False

    pattern = (
        r"^[A-Za-z0-9._%+-]+@"
        r"[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    )

    return bool(re.fullmatch(pattern, email))


def validate_age(age):
    try:
        if isinstance(age, bool):
            return False

        age = int(age)
        return 1 <= age <= 120

    except (ValueError, TypeError):
        return False
