from lib import connection_object as conn
import psycopg2
import psycopg2.extras


class PostgresClient:
    """
    singleton class for postgres client
    """
    @staticmethod
    def execute_cursor(script: str):
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute(script)
        conn.commit()

    @staticmethod
    def read_execute_cursor(script: str):
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute(script)
            return cur.fetchall()

    @staticmethod
    def create_table(table: str, columns: list):
        '''
        This function will create a new table in postgres database,
        by getting tablename, columns with dataTypes
        '''
        create_table_script = f'CREATE TABLE IF NOT EXISTS {table}' +\
            f' ({", ".join(columns)})'
        PostgresClient.execute_cursor(create_table_script)

    @staticmethod
    def insert(table: str, columns: list, values: list):
        '''
        This function will insert values in postgres database table,
        by getting tablename, columns and values as parameter
        '''
        value_list = ""
        for value in values:
            value_list = value_list + "'" + value + "',"

        insert_script = f'INSERT INTO {table}' +\
            f' ({", ".join(columns)})' +\
            f' VALUES ({value_list[:-1]})'
        PostgresClient.execute_cursor(insert_script)

    @staticmethod
    def update(table: str, statement_list: dict, filter: dict):
        '''
        This function will update values in postgres database table,
        by getting tablename, columns and values as parameter
        '''
        statement = ""
        for key, value in statement_list.items():
            statement = statement + f"{key} = '{value}', "

        filter_statement = ""
        for key, value in filter.items():
            filter_statement = filter_statement + f"{key} = '{value}' AND "

        update_script = f'UPDATE {table} SET' +\
            f' {statement[:-2]}' +\
            f' WHERE {filter_statement[:-5]}'
        PostgresClient.execute_cursor(update_script)

    @staticmethod
    def read(table: str, columns: list = [], filter: dict = []):
        '''
        This function fetches values from postgres database table
        '''
        columns_list = ""
        for column in columns:
            columns_list = columns_list + f", {column}"

        filter_statement = ""
        if filter == []:
            filter_statement = "1 = 1"
        else:
            for key, value in filter.items():
                filter_statement = filter_statement + f"{key} = '{value}' AND "
            filter_statement = filter_statement[:-5]

        columns_list = "*" if columns_list == "" else columns_list

        read_script = f'SELECT {columns_list[:2]} FROM {table}' +\
            f' WHERE {filter_statement}'
        return PostgresClient.read_execute_cursor(read_script)

    @staticmethod
    def delete(table: str, filter: dict):
        '''
        This function marks the records as deleted in postgres database table
        '''
        filter_statement = ""
        if filter == {}:
            filter_statement = "1 = 1"
        else:
            for key, value in filter.items():
                filter_statement = filter_statement + f"{key} = '{value}' AND "
            filter_statement = filter_statement[:-5]

        delete_script = f'UPDATE {table} ' +\
            ' SET is_deleted = TRUE' +\
            f' WHERE {filter_statement}'
        PostgresClient.execute_cursor(delete_script)

    @staticmethod
    def get_row_count(table: str):
        read_script = f'SELECT COUNT(*) FROM {table} WHERE is_deleted = FALSE'
        return PostgresClient.read_execute_cursor(read_script)[0][0]

    @staticmethod
    def drop_table(table: str):
        drop_script = f'DROP TABLE IF EXISTS {table}'
        return PostgresClient.execute_cursor(drop_script)
