
import bcrypt


def hash_password(password):
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt(rounds=12)

    return bcrypt.hashpw(password_bytes, salt)


def verify_password(password, stored_hash):
    try:
        password_bytes = password.encode("utf-8")

        return bcrypt.checkpw(
            password_bytes,
            stored_hash
        )

    except (ValueError, TypeError):
        return False
