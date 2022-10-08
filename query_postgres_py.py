
import psycopg2
from config import host, user, password, db_name, port

# В try подключение к БД и запросы к таблицам
try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=db_name,
        port=port
    )

    # the cursor for performing database operator
    cursor = connection.cursor()

    cursor.execute(
        """CREATE TABLE users(
            id serial PRIMARY KEY,
            nick_name varchar(50) NOT NULL,
            login varchar(50) NOT NULL)"""
    )

    connection.commit()
    print('create table sucesfully')

except Exception as _ex:
    print('[INFO] Error while working with PostgreSQL', _ex)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('[INFO] PostgreSQL connection closed')
