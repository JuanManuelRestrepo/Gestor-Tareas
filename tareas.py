from Menu import *

class Tarea():

    #Metodo constructopr, con sus atributos
    def __init__(self, titulo, descripcion,Responsable_correo, fecha_limite):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.responsable=Responsable_correo
        self.estado = "Pendiente"

