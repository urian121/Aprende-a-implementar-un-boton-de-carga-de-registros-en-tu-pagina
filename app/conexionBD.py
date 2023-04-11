#Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector

def connectionBD():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="demo",
            #auth_plugin='mysql_native_password',
            #charset='utf8mb4',
            #collation='utf8mb4_unicode_ci'
        )
        if mydb.is_connected():
            print("Conexión exitosa a la base de datos")
            return mydb
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")