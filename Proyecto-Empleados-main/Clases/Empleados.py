import hashlib
import departamentos
from datetime import datetime

class empleados():
    def __init__(self, id, nombre, direccion, telefono, correo, fecha_inicio, salario, id_tipo, rut, contraseña):
        super().__init__(id, nombre, telefono)
        self._direccion = direccion
        self._correo = correo
        self._fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        self._salario = salario
        self._id_tipo = id_tipo 
        self._rut = rut
        self.__contraseña = self._encriptar(contraseña)

    def guardar_empleado(self, departamento):
        
        print(f"Guardando el empleado {self._nombre} en el sistema...")

    
        departamento.asignar_gerente(self)

    def validar_datos(self):
        return all([self._nombre, self._telefono, self._correo, self._fecha_inicio, self._salario, self._rut])

    def _encriptar(self, contraseña):
        return hashlib.sha256(contraseña.encode()).hexdigest()

    def validar_contraseña(self, contraseña):
        return self.__contraseña == hashlib.sha256(contraseña.encode()).hexdigest()

    def detalles(self):
        return (super().detalles() +
                f", Dirección: {self._direccion}, Correo: {self._correo}, Salario: {self._salario}")


departamento_ventas = departamentos(id=1, nombre="Ventas", telefono="123-456-789")

empleado_gerente = empleados(
    id=1, nombre="Carlos Perez", direccion="Calle Falsa 123", telefono="987-654-321",
    correo="carlos@example.com", fecha_inicio="2023-01-01", salario=5000,
    id_tipo="Gerente", rut="12345678-9", contraseña="securepass"
)

empleado_gerente.guardar_empleado(departamento_ventas)
print(departamento_ventas.detalles())