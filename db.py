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


connection = create_connection("db4free.net", "dgu_soc", "fmikn_social", "autorization_bd")

admin = ('user1', 123456)

mycursor = connection.cursor()
mycursor.execute('SELECT user_name, user_pass FROM users')
myresult = mycursor.fetchall()
print(myresult)

if admin in myresult:
    print("YES")
else:
    print("NO")



#if admin.split(',') in myresult[0]:
#    print('YES')
#else:
#    print('NO')

#sqlFormula = 'INSERT INTO users (id, user_name, user_pass) VALUES (%s, %s, %s)'
#user1 = (1, 'user1', 123456)
#mycursor.execute(sqlFormula, user1)
#connection.commit()


#def create_database(connection, query):
#    cursor = connection.cursor()
#    try:
#        cursor.execute(query)
#        print("DB create successfully!")
#    except Error as e:
#        print(f"The Error '{e}' occurred")
#
#
#create_database_query = "CREATE DATABASE sm_app"
#create_database(connection, create_database_query)
