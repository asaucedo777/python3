import psycopg2

def get_connection():
  try:
    connection = psycopg2.connect(
      dbname='test',
      user='test',
      password='test',
      host='localhost',
      port='5432',
    )
    print('Connection successfully!')
    return connection
  except psycopg2.Error as e:
    print(f'Something went wrong {e.message}')
  finally:
    print('The try except is finished')

def get_cursor(connection):
  cursor = connection.cursor()
  return cursor

def drop_table(cursor, table_name):
  cursor.execute(f'DROP TABLE IF EXIST {table_name}')

types_map = {
  'StringType': 'varchar(1000)',
  'IntegerType': 'varchar(1000)',
}

def build_fields_declaration(schema):
  fields_declaration = ''
  schema.fields.foreach(lambda f:
    fields_declaration.append(f'{f.name} {types_map[f.dataType.__str__()]}')
  )
  return fields_declaration

def create_table(cursor, table_name, schema):
  fields_declaration = build_fields_declaration(schema)
  fields = ', '.join([item for item in fields_declaration])
  sql_create = f'CREATE TABLE {table_name} ({fields})'
  cursor.execute(sql_create)
  return fields_declaration

def close_db(connection, cursor):
  try:
    cursor.close()
  except:
    print('Something went wrong')
  finally:
    connection.close()
    print('The try except is finished')