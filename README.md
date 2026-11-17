# Week 5 – Security Enhancements in Python Applications

## Project Overview
This project demonstrates security improvements in a Python-based Student Management Application. It provides user registration, secure login, and student record management using SQLite.

## Features
- Secure password hashing using bcrypt.
- Password verification.
- Username and password validation.
- Student name, email, and age validation.
- Parameterized SQL queries to prevent SQL injection.
- SQLite database with unique constraints.
- Automated unit testing.
- Security scanning using Bandit.
- Dependency vulnerability scanning using pip-audit.

## Technologies Used
- Python 3.14
- SQLite
- bcrypt
- unittest
- Bandit
- pip-audit

## Project Structure
```text
Week5_Security_Enhancements/
├── README.md
├── requirements.txt
├── reports/
│   └── Week5_Security_Audit_Report.docx
├── secure_app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── security.py
│   └── validators.py
└── tests/
    ├── test_application.py
    └── test_security.py
```

## Installation

Install the dependencies:

```bash
py -m pip install -r requirements.txt
```

## Run the Application

```bash
py -m secure_app.main
```

## Run Unit Tests

```bash
py -m unittest discover -s tests -v
```

## Security Audit Commands

Run Bandit:

```bash
py -m bandit -r secure_app
```

Run dependency audit:

```bash
py -m pip_audit
```

## Security Testing Results

- Unit tests: 14 passed.
- Bandit: No issues identified.
- pip-audit: No known vulnerabilities found after upgrading Pillow to 13.0.0.

## Conclusion

The project applies important Python application security practices, including password hashing, input validation, parameterized SQL queries, and dependency vulnerability checking. All 14 automated tests passed, and the final security scans reported no known issues.

## Author
Logendra Prabhu V"# Week5-Security-Enhancements" 
"# Week6-CI-Integration" 
