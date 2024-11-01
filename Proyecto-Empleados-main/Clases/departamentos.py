class departamento:
    def __init__(self, id, nombre, telefono):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.gerente = None 

    def asignar_gerente(self, empleado):
       if empleado.id_tipo == "gerente":
        self.gerente = empleado
        print(f"Empleado {empleado.nombre} ha sido asignado como gerente del departamento {self._nombre}")
        
       else:
           print(f"Empleado {empleado.nombre} no tiene el rol de gerente del departamento")
            
    def detalles(self):
       gerente_info = f"gerente: {self.gerente.nombre}" if self.gerente else "gerente: No asignado"
       return f"Departamento ID: {self.id}, Nombre: {self.nombre}, Telefono {self.telefono},Informacion Gerente {gerente_info}"
    
    