from abc import ABC, abstractclassmethod
from Menu import *

class TareaBase(ABC):

    #Metodo constructopr, con sus atributos
    def __init__(self, titulo, descripcion,Responsable_correo, fecha_limite):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.responsable=Responsable_correo
        self.estado = "Pendiente"

    @abstractclassmethod
    def cambiar_estado(self, nuevo_estado):
        pass
    
class Tarea(TareaBase):

    def cambiar_estado(self, nuevo_estado):
        self.estado=nuevo_estado

    def __str__(self):
        return (f"TAREA\n"
                f"Título: {self.titulo}\n"
                f"Descripción: {self.descripcion}\n"
                f"Responsable: {self.responsable.nombre}\n"
                f"Fecha Límite: {self.fecha_limite}\n"
                f"Estado: {self.estado}")