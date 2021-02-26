import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("Successful connect!")
    except Error as e:
        print(f"Error '{e}' occurred")

    return connection


#def create_database(connection, query):
#    cursor = connection.cursor()
#    try:
#        cursor.execute(query)
#        print("DB create successfully!")
#    except Error as e:
#        print(f"The Error '{e}' occurred")
#
#

