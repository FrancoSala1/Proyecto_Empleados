class Departamento_empleado:
    def __init__(self, id, id_depto, id_empleado):
        self.id = id
        self.id_depto = id_depto
        self.id_empleado = id_empleado

    def validar_asignacion(self):
        return self.id_empleado is not None and self.id_depto is not None
