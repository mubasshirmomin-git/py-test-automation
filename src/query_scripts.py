# Queries for Setup
# Test table name & operations
test_table_name = 'my_table'


create_table_query = f''' CREATE TABLE IF NOT EXISTS {test_table_name} (
                                id int PRIMARY KEY,
                                name varchar(40) NOT NULL,
                                designation varchar(40) NOT NULL,
                                is_deleted BOOLEAN DEFAULT FALSE)'''

drop_old_table_query = f'DROP TABLE IF EXISTS {test_table_name}'

insert_data_query  = f'INSERT INTO {test_table_name} (id, name, designation) VALUES (%s, %s, %s)'
insert_values = [(1, 'Tom Hardy', 'Data Engineer'), (2, 'Hugh Jackman','Data Engineer' ), (3, 'Morgan Freeman', 'Data Analyst')]

extract_schema_query = f""" SELECT column_name, data_type
                                        FROM information_schema.columns
                                        WHERE table_name = '{test_table_name}'"""

# New Test table which will be created from taking schema from old test table
new_test_table_name = 'my_table_copy'
drop_new_table_query = f'DROP TABLE IF EXISTS {new_test_table_name}'



# Queries for testing

# Insert, Update & Delete test queries
select_data_query = f"SELECT name FROM {test_table_name} WHERE id = 1"
count_rows_query = f'SELECT COUNT(*) FROM {test_table_name}'
update_data_query = f"UPDATE {test_table_name} SET name = 'Tom Hanks' WHERE id = 1"
delete_data_query = f"DELETE FROM  {test_table_name} WHERE id = 2"

# Compare schemas test queries
table_details_query_original_table = f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{test_table_name}'"
table_details_query_new_table = f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{new_test_table_name}'"

# Alter table test queries
new_column_name = 'department'
add_column_query = f'ALTER TABLE {test_table_name} ADD COLUMN {new_column_name} VARCHAR(50)'
new_column_check_query = f"SELECT column_name FROM information_schema.columns WHERE table_name = '{test_table_name}' AND column_name = '{new_column_name}'"