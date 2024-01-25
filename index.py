from postgres import PostgresClient as pg
from utils import Utils
table_name = 'person'
table_columns = ['id int PRIMARY KEY',
                 'name varchar(40) NOT NULL',
                 'designation varchar(40) NOT NULL',
                 'is_deleted BOOLEAN DEFAULT FALSE']


class person:
    def create_table():
        """
        This function will create table name person if it not already exists
        """
        try:
            pg.create_table(table_name, table_columns)
        except Exception as error:
            print(error)

    def test_insert():
        """
        This function will help to insert values into the table
        """
        try:
            id = Utils.convertNULLtoInteger(str(input('Id: ')))
            name = str(input('Name: '))
            designation = str(input('Designation: '))

            if id == 0 or name == "":
                return print('Inputs not available.')

            initial_rows = pg.get_row_count(table_name)
            pg.insert(table_name, ['id', 'name', 'designation'],
                      [str(id), name, designation])
            updated_rows = pg.get_row_count(table_name)
            assert initial_rows != updated_rows, "Data insertion failed"
            assert initial_rows + 1 == updated_rows, "Incorrect " +\
                "number of row(s) inserted"
            print('Data inserted successfully.')
        except Exception as error:
            print(error)

    def test_update():
        """
        This function will update any row on specific conditions
        """
        try:
            id = Utils.convertNULLtoInteger(str(input('Id: ')))
            name = str(input('Name: '))
            if id == 0 or name == "":
                return print('Inputs not available.')

            initial_data = pg.read(table_name)
            pg.update(table_name, {"name": name}, {"id": id})
            updated_data = pg.read(table_name)
            assert initial_data != updated_data, "Data updation failed"
            print('Data updated successfully.')
        except Exception as error:
            print(error)

    def getPersonDetails():
        """
        This function will help in extracting any details on id
        """
        try:
            id = Utils.convertNULLtoInteger(str(input('Id: ')))
            if id == 0:
                return print('Inputs not available.')

            persons = pg.read(table_name, filter={'id': id})
            print(persons)
        except Exception as error:
            print(error)

    def deletePersonFromDB():
        """
        This function will delete any records on id
        """
        try:
            id = Utils.convertNULLtoInteger(str(input('Id: ')))
            if id == 0:
                return print('Inputs not available.')

            pg.delete(table_name, filter={'id': id})
            rows = pg.get_row_count(table_name)
            print(rows)
            assert rows > 0, "Blank table"
        except Exception as error:
            print(error)


person.test_update()
