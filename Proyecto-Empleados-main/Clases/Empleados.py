import hashlib
from datetime import datetime

class Empleados:
    def __init__(self, id, nombre, direccion, telefono, correo, fecha_inicio, salario, id_tipo, rut, contraseña):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        self.salario = salario
        self.id_tipo = id_tipo
        self.rut = rut
        self.contraseña = self.encriptar(contraseña)

    def validar_datos(self):
        return all([self.nombre, self.telefono, self.correo, self.fecha_inicio, self.salario, self.rut])

    def encriptar(self, contraseña):
        return hashlib.sha256(contraseña.encode()).hexdigest()

    def desencriptar(self, contraseña_encriptada):
        return False
