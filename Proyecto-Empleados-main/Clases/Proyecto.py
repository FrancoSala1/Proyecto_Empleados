from datetime import datetime

class Proyecto:
    def __init__(self, id, nombre, descripcion, fecha_inicio, fecha_fin):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        self.fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')

    def validar_fechas(self):
        return self.fecha_inicio < self.fecha_fin
