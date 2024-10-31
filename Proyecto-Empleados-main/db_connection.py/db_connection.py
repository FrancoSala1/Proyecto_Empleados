import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Usuario por defecto en XAMPP
            password='',  # Sin contraseña por defecto
            database='gestion_empleados'
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
    except Error as e:
        print(f"Error: {e}")
    return connection
