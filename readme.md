# PyTest PostgreSQL Automation Script

## Overview

This repository contains an automation script written in Python using PyTest for testing PostgreSQL database functionality. The script is designed to streamline the testing process, providing a convenient and efficient way to ensure the reliability and correctness of your PostgreSQL database operations.

## Prerequisites

Before running the script, make sure you have the following installed:

Python (version 3.10 or higher)
PyTest
PostgreSQL database server
psycopg2 library (for PostgreSQL connectivity)

## Project Structure

The project is organized into the following directories:

- `src`: Contains Python scripts for database operations and setup (`db_test_setup.py`), and queries for different operations (`query_scripts.py`).
- `tests`: Includes test script for database connection and DDL/DML operations (`test_db.py`).
- `config.py`: Configuration file for project options.
- `requirements.txt`: List of dependencies.
- `README.md`: Project documentation.

## Installation

1. Clone the repository:

- `git clone https://github.com/mubasshirmomin-git/py-test-automation.git`

2. Install dependencies:

- `pip install -r requirements.txt`

3. Configure the database connection in the config.py file.

## Configuration

Modify the config.py file to set the appropriate values for your local PostgreSQL database:

host : 'localhost',
database : 'postgres',
username : 'postgres',
password : 'postgres',
port_id : 5433

## Running Tests

To run the PyTest script, use the following command:

- `pytest tests/test_db.py --verbose`

## Test Cases

The script includes test cases for various PostgreSQL operations, such as:

- Connection establishment
- CRUD operations (Create, Read, Update, Delete)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create an issue or submit a pull request.
