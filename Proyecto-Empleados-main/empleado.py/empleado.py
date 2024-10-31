import mysql.connector
from mysql.connector import Error

class Empleado:
    def __init__(self, id, nombre, direccion, telefono, correo, fecha_inicio, salario, id_tipo, rut, contraseña):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.fecha_inicio = fecha_inicio
        self.salario = salario
        self.id_tipo = id_tipo
        self.rut = rut
        self.contraseña = contraseña

    def validar_datos(self):
        # Aquí puedes agregar lógica para validar datos
        pass

    def encriptar_contraseña(self):
        import hashlib
        return hashlib.sha256(self.contraseña.encode()).hexdigest()
