from datetime import datetime

class Registro_tiempo:
    def __init__(self, id, fecha, tareas, id_asignacion, observacion):
        self.id = id
        self.fecha = datetime.strptime(fecha, '%Y-%m-%d')
        self.tareas = tareas
        self.id_asignacion = id_asignacion
        self.observacion = observacion

    def validar_horas(self):
        return True
