import psycopg2
from config import Config

connection_string = Config.getConnectionString('local')
connection_object = psycopg2.connect(host=connection_string['host'],
                                     dbname=connection_string['database'],
                                     user=connection_string['username'],
                                     password=connection_string['password'],
                                     port=connection_string['port_id'])
