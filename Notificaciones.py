from Correo import *
from abc import ABC, abstractclassmethod
from gestor import *

correo=Correo_gmail('ayalajuanma1213@gmail.com', 'pqdz diwr wwtq crcs')
class Notificacion_Base(ABC):
    def __init__(self):
        self.correo=correo
    @abstractclassmethod
    def notificar_Nueva_Tarea(self):
        pass
    @abstractclassmethod
    def notificar_Tarea_Terminada(self):
        pass
    @abstractclassmethod
    def notificar_Tarea_Cambios(self):
        pass

class Notificacion(Notificacion_Base):
    def notificar_Nueva_Tarea(self, tarea):
        print("Se ha creado una nueva tarea")
        cuerpo = f"Se ha creado una nueva tarea:\nTítulo: {tarea.titulo}\nDescripción: {tarea.descripcion}\nFecha límite: {tarea.fecha_limite}\nEstado: {tarea.estado}"
        self.correo.enviar_correo(tarea.responsable.correo_electronico, f"Nueva Tarea: {tarea.titulo}", cuerpo)
        print("Notificación de nueva tarea enviada.")

    def notificar_Tarea_Terminada(self, tarea):
        cuerpo = f"La tarea ha sido marcada como terminada:\nTítulo: {tarea.titulo}\nDescripción: {tarea.descripcion}\nFecha límite: {tarea.fecha_limite}\nEstado: {tarea.estado}"
        self.correo.enviar_correo(tarea.responsable.correo_electronico, f"Tarea Terminada: {tarea.titulo}", cuerpo)
        print("Notificación de tarea terminada enviada.")
    
    def notificar_Tarea_Cambios(self, tarea):
        cuerpo = f"La tarea ha sido actualizada:\nTítulo: {tarea.titulo}\nDescripción: {tarea.descripcion}\nFecha límite: {tarea.fecha_limite}\nEstado: {tarea.estado}"
        self.correo.enviar_correo(tarea.responsable.correo_electronico, f"Cambios en la Tarea: {tarea.titulo}", cuerpo)
        print("Notificación de cambios en la tarea enviada.")


