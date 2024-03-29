import pytest
from src.db_test_setup import db_connection, create_and_insert
from src.query_scripts import test_table_name, new_test_table_name, select_data_query, count_rows_query, update_data_query, delete_data_query, table_details_query_original_table, table_details_query_new_table, new_column_name, add_column_query, new_column_check_query


def test_postgresql_connection(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    assert result[0] == 1
    cursor.close()


def test_table_creation(db_connection):
    """
    Test if the table is created or not
    """
    with db_connection.cursor() as cur:
        cur.execute(table_details_query_original_table)
        table_exists = len(cur.fetchone()) > 0
        
        assert table_exists, f"Table '{test_table_name}' not created successfully"


def test_data_inserted(db_connection):
    """
        Test  the data inserted checking the record counts
    """
    with db_connection.cursor() as cur:
        cur.execute(count_rows_query)
        count = cur.fetchone()[0]
        assert count == 3, 'Incorrect number of rows inserted'


def test_data_updated(db_connection):
    """
    Update a record & test the output
    """
    # Updating Name of one record
    with db_connection.cursor() as cur:
        cur.execute(update_data_query)
    db_connection.commit()

    # Fetching name of the updated table & comparing with desired output
    with db_connection.cursor() as cur:
        cur.execute(select_data_query)
        val = cur.fetchone()[0]
        assert val == 'Tom Hanks', 'Data is not updated successfully'


def test_delete(db_connection):
    """
    Delete one record & test the output, no of records after deletion should be 2
    """
    with db_connection.cursor() as cur:
        cur.execute(delete_data_query)
    db_connection.commit()

    with db_connection.cursor() as cur:
        cur.execute(count_rows_query)
        count = cur.fetchone()[0]
        assert count == 2, "Incorrect number of rows after delete"


def test_compare_schemas(db_connection):
    """
    Compare the schemas between old & new test columns
    """
    with db_connection.cursor() as cur:
        # Extract schema from 'test_table'
        cur.execute(table_details_query_original_table)
        expected_schema = cur.fetchall()

        # Extract schema from 'another_table'
        cur.execute(table_details_query_new_table)
        new_schema = cur.fetchall()

        assert expected_schema == new_schema, f"Schemas of '{test_table_name}' and '{new_test_table_name}' do not match"


def test_new_column_added(db_connection):
    """
    Add a new column in old test table & test it
    """

    # Add new column to the old test table
    with db_connection.cursor() as cur:
        cur.execute(add_column_query)
    db_connection.commit()

    # Check if the new_column exists in old test table
    with db_connection.cursor() as cur:
        cur.execute(new_column_check_query)
        new_column_exists = cur.fetchone() is not None

        assert new_column_exists, f"New column '{new_column_name}' not added to '{test_table_name}' successfully"
