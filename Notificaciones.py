from Correo import *
from abc import ABC, abstractclassmethod
from gestor_tareas import *
from tareas import *
from BasesdeDatos import *

correo=Correo_gmail('ayalajuanma1213@gmail.com', 'pqdz diwr wwtq crcs')
class Notificacion_Base(ABC):
    def __init__(self):
        self.correo=correo
        self.DB=DatabaseManager()
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
        self.correo.enviar_correo(tarea.responsable_correo, f"Nueva Tarea: {tarea.titulo}", cuerpo)
        print("Notificación de nueva tarea enviada.")

    def notificar_Tarea_Terminada(self,titulo):
        datos=self.DB.notificar_tarea_terminada(titulo)
        if datos:
            titulo, descripcion, correo = datos
            cuerpo = f"La tarea ha sido marcada como terminada:\nTítulo: {titulo}\nDescripción: {descripcion}"
            self.correo.enviar_correo(correo, f"Tarea Terminada: {titulo}", cuerpo)
            print("Notificación de tarea terminada enviada.")
    
    def notificar_Tarea_Cambios(self, titulo_notificar):
        resultado = self.DB.notificacion_cambio_tarea(titulo_notificar)
        if resultado:
            titulo, descripcion,fecha_limite,estado,correo= resultado
            # Realiza operaciones con los valores desempaquetados
            cuerpo=f"Tarea actualizada:\nTítulo: {titulo}\nDescripción: {descripcion}\nFecha límite: {fecha_limite}\nEstado: {estado}"
            self.correo.enviar_correo(correo, f"Tarea Actualizada: {titulo}", cuerpo)
        else:
            print("No se encontró la tarea para notificar o hubo un error en la consulta.")
