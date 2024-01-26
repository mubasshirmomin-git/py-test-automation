import pytest
from db_test_setup import db_connection, create_and_insert, test_table_name, new_test_table_name


count_rows_query = f'SELECT COUNT(*) FROM {test_table_name}'
update_data_query = f"UPDATE {test_table_name} SET name = 'Rehman Ali' WHERE id = 1"
select_data_query = f"SELECT name FROM {test_table_name} WHERE id = 1"
delete_data_query = f"DELETE FROM  {test_table_name} WHERE id = 2"

table_details_query_new_table = f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{new_test_table_name}'"

new_column_name = 'department'
add_column_query = f'ALTER TABLE {test_table_name} ADD COLUMN {new_column_name} VARCHAR(50)'
new_column_check_query = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{test_table_name}' AND column_name = '{new_column_name}'"


# DDL Test cases
def test_table_existance(db_connection):
    """
    Test if the table is created or not
    """
    with db_connection.cursor() as cur:
        cur.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{test_table_name}'")
        table_exists = len(cur.fetchone()) > 0

        assert table_exists, f"Table '{test_table_name}' does not exist"


def test_compare_schemas(db_connection):
    """
    Compare the schemas between old & new test columns
    """
    with db_connection.cursor() as cur:
        # Extract schema from 'test_table'
        cur.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{test_table_name}'")
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


# DML test function
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
        assert val == 'Rehman Ali', 'Data is not updated successfully'


def test_data_delete(db_connection):
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