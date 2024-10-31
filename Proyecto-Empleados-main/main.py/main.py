from db_connection import create_connection
from empleado import Empleado

def main():
    # Intenta crear una conexión a la base de datos
    connection = create_connection()

    # Ejemplo de creación de un nuevo empleado
    if connection:
        nuevo_empleado = Empleado(
            id=None,  # ID será asignado automáticamente
            nombre="Juan Pérez",
            direccion="Calle Falsa 123",
            telefono="123456789",
            correo="juan.perez@example.com",
            fecha_inicio="2023-10-01",
            salario=3000.00,
            id_tipo=1,
            rut="12345678-9",
            contraseña="mi_contraseña"
        )
        # Aquí puedes agregar lógica para guardar el nuevo empleado en la base de datos

        connection.close()  # Cierra la conexión después de usarla

if __name__ == "__main__":
    main()
