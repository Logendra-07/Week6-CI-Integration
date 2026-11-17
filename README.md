# Week 6 – Continuous Integration (CI) in Python Projects

## Project Overview

This project demonstrates the implementation of Continuous Integration (CI) in a Python application using GitHub Actions. It automates code quality checks and unit testing whenever changes are pushed to the GitHub repository.

## Objectives

- Implement an automated CI pipeline.
- Execute Python unit tests automatically.
- Perform code quality checks using Flake8.
- Generate test and code coverage reports.
- Upload test reports as GitHub Actions artifacts.

## Technologies Used

- Python 3.14
- Git and GitHub
- GitHub Actions
- Pytest
- Pytest-Cov
- Flake8
- SQLite
- bcrypt

## Project Structure

```text
Week6_CI_Integration/
├── .github/
│   └── workflows/
│       └── python-ci.yml
├── reports/
├── secure_app/
│   ├── database.py
│   ├── main.py
│   ├── security.py
│   └── validators.py
├── tests/
│   ├── test_application.py
│   └── test_security.py
├── .gitignore
├── requirements.txt
└── README.md
```

## CI Pipeline

The GitHub Actions workflow performs the following steps:

1. Checks out the source code.
2. Sets up Python 3.14.
3. Installs project dependencies.
4. Checks code quality using Flake8.
5. Executes automated tests using Pytest.
6. Generates XML test and coverage reports.
7. Uploads reports as workflow artifacts.

## Running Locally

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run code quality checks:

```bash
python -m flake8 secure_app tests --count --show-source --statistics
```

Run automated tests:

```bash
python -m pytest tests -v
```

Generate coverage reports:

```bash
python -m pytest tests -v --cov=secure_app --cov-report=term --cov-report=xml:reports/coverage.xml
```

## Test Results

- Total automated tests: 14
- Passed tests: 14
- Failed tests: 0
- Flake8 errors: 0
- Overall code coverage: 38%

## GitHub Repository

https://github.com/Logendra-07/Week6-CI-Integration

## Conclusion

This project demonstrates how Continuous Integration improves software development by automating testing and code