
import sqlite3


from .database import (
    initialize_database,
    create_user,
    get_user,
    add_student,
    get_students
)

from .security import hash_password, verify_password

from .validators import (
    validate_username,
    validate_password,
    validate_name,
    validate_email,
    validate_age
)


def register():
    print("\n--- User Registration ---")

    username = input("Enter username: ").strip()
    password = input("Enter password: ")

    if not validate_username(username):
        print("Invalid username. Use 3-30 letters, numbers or underscores.")
        return

    if not validate_password(password):
        print("Password must contain 8-72 UTF-8 bytes.")
        return

    password_hash = hash_password(password)

    if create_user(username, password_hash):
        print("Registration successful!")
    else:
        print("Registration failed. Username may already exist.")


def login():
    print("\n--- User Login ---")

    username = input("Enter username: ").strip()
    password = input("Enter password: ")

    user = get_user(username)

    if user and verify_password(password, user["password_hash"]):
        print("Login successful!")
        return True

    print("Invalid username or password.")
    return False


def add_student_record():
    print("\n--- Add Student ---")

    name = input("Enter student name: ").strip()
    email = input("Enter student email: ").strip()
    age = input("Enter student age: ").strip()

    if not validate_name(name):
        print("Invalid student name.")
        return

    if not validate_email(email):
        print("Invalid email address.")
        return

    if not validate_age(age):
        print("Invalid age.")
        return

    try:
        add_student(name, email, int(age))
        print("Student added successfully!")

    except sqlite3.IntegrityError:
        print("Unable to add student. Email may already exist.")

    except sqlite3.Error:
        print("Database operation failed.")


def display_students():
    print("\n--- Student Records ---")

    try:
        students = get_students()

        if not students:
            print("No student records found.")
            return

        for student in students:
            print(
                f"ID: {student['id']} | "
                f"Name: {student['name']} | "
                f"Email: {student['email']} | "
                f"Age: {student['age']}"
            )

    except sqlite3.Error:
        print("Unable to retrieve student records.")


def student_menu():
    while True:
        print("\n===== SECURE STUDENT MANAGEMENT =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student_record()

        elif choice == "2":
            display_students()

        elif choice == "3":
            print("Logged out successfully.")
            break

        else:
            print("Invalid choice. Try again.")


def main():
    initialize_database()

    while True:
        print("\n===== SECURE STUDENT MANAGEMENT SYSTEM =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register()

        elif choice == "2":
            if login():
                student_menu()

        elif choice == "3":
            print("Application closed.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nApplication terminated safely.")

    except sqlite3.Error:
        print("A database error occurred.")
