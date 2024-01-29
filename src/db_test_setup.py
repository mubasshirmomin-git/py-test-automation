import pytest
import psycopg2
import psycopg2.extras
from config import Config
from src.query_scripts import create_table_query, drop_old_table_query, insert_data_query, insert_values, extract_schema_query, drop_new_table_query, new_test_table_name

connection_string = Config.getConnectionString('local')

# Pytest fixtures for database setup and other operations 
@pytest.fixture(scope="module")
def db_connection():
    # Create a connection to the test database
    conn = psycopg2.connect(host=connection_string['host'],
                            dbname=connection_string['database'],
                            user=connection_string['username'],
                            password=connection_string['password'],
                            port=connection_string['port_id'])
    yield conn

    # Close the connection after all tests
    conn.close()


# Function to extract schema from old test table and create another table
def create_table_with_same_schema(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute(extract_schema_query)
        columns_info = cursor.fetchall()

        # Create another table with the same schema
        create_new_table_query = f"CREATE TABLE IF NOT EXISTS {new_test_table_name} ("
        for column_info in columns_info:
            column_name, data_type = column_info
            create_new_table_query += f"{column_name} {data_type}, "
        create_new_table_query = create_new_table_query.rstrip(", ") + ");"

        cursor.execute(create_new_table_query)
    db_connection.commit()


@pytest.fixture(scope="function", autouse=True)
def create_and_insert(db_connection):
    with db_connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

        # Drop the tables if exists
        cur.execute(drop_old_table_query)
        cur.execute(drop_new_table_query)

        # Create new table
        cur.execute(create_table_query)

        # insert data into table
        for record in insert_values:
            cur.execute(insert_data_query, record)

        # Create another table with the same schema
        create_table_with_same_schema(db_connection)

    db_connection.commit()

    # Yield to the test
    yield

    # Drop the tables after each test
    with db_connection.cursor() as cur:
        cur.execute(drop_old_table_query)
        cur.execute(drop_new_table_query)
    db_connection.commit()
