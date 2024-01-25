### This Python project interacts with a PostgreSQL database, running both DML (Data Manipulation Language) and DDL (Data Definition Language) queries.

- Key Features:
  Connects to a PostgreSQL database.
  Executes DML queries including:
  INSERT: Adds new data to existing tables.
  UPDATE: Modifies existing data in tables.
  DELETE: Removes data from tables.
  SELECT: Retrieves data from tables using various filters and join operations.
  Executes DDL queries including:
  CREATE: Creates new tables, databases, or other schema objects.
  ALTER: Modifies existing schema objects.
  DROP: Deletes existing schema objects.
  Provides error handling and logging mechanisms.
  (Optional) Offers additional functionalities like:
  Parameterized queries for dynamic execution.
  Transactions for data consistency.
  Integration with data visualization tools.

- Requirements:
  Python 3.8.10
  psycopg2 library for PostgreSQL communication
  PostgreSQL database v16

- Getting Started:
  Install dependencies: pip install -r requirements.txt
  Configure database connection details in the project.
  Run the main script: python index.py
