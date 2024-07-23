from Menu import *
from datetime import datetime

class Tarea():

    #Metodo constructopr, con sus atributos
    def __init__(self, titulo, descripcion,Responsable_correo, fecha_limite):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_limite = datetime.strptime(fecha_limite, "%Y-%m-%d")  # Convertir string a datetime
        self.responsable=Responsable_correo
        self.estado = "Pendiente"

