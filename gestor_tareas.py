from abc import ABC, abstractclassmethod
from tareas import*
from Correo import *
from Notificaciones import *
from BasesdeDatos import DatabaseManager as DB

notificacion=Notificacion()
class Gestor_usuarios_Base(ABC):

    @abstractclassmethod
    def Agregar_Tarea(self):
        pass

    @abstractclassmethod
    def Eliminar_tarea(self):
        pass
    @abstractclassmethod
    def Actualizar_tarea(self):
        pass
    @abstractclassmethod
    def listar_tareas(self):
        pass
    @abstractclassmethod
    def Tarea_usuario(self):
        pass
    @abstractclassmethod
    def Terminar_tarea(self):
        pass

class Gestor_Tareas(Gestor_usuarios_Base):

    def __init__(self):
        self.notificacidor=notificacion
        self.DB=DB()

    def Agregar_Tarea(self, tarea):
        #misma comprobancion anterior
        if not isinstance(tarea, Tarea):
            raise ValueError(" EL objeto no es una instacia de la clase Tarea")
        tarea_existente=self.DB.validar_tarea(tarea.titulo)
        if not tarea_existente:
            self.DB.agregar_tarea(tarea.titulo, tarea.descripcion, tarea.fecha_limite,tarea.estado,tarea.responsable_correo)
            self.notificacidor.notificar_Nueva_Tarea(tarea)
        else:
            print(f"Tarea : {tarea.titulo} existente")

    def listar_tareas(self):
        self.DB.listar_tareas()

    def Eliminar_tarea(self,titulo):
            self.DB.eliminar_tarea(titulo)
            
    def Actualizar_tarea(self, tarea_titulo): 
        nuevo_titulo=input("Digite el nuevo nombre")
        nueva_descripcion=input("Digite la descripcion")
        while True:
            nueva_fecha_limite_str = input("Digite la nueva fecha límite (YYYY-MM-DD): ")
            try:
                nueva_fecha_limite = datetime.strptime(nueva_fecha_limite_str, "%Y-%m-%d")
                break
            except ValueError:
                print("Formato de fecha no válido. Inténtelo de nuevo.")
        responsable_correo=input("Digite el correo del responsable")
        self.DB.Actualizar_tarea(tarea_titulo, nuevo_titulo,nueva_descripcion,nueva_fecha_limite,responsable_correo)
        self.notificacidor.notificar_Tarea_Cambios(nuevo_titulo)

    def listar_tareas(self):
       self.DB.listar_tareas()

    def Tarea_usuario(self, correo_responsable):
        validacion_correo=self.DB.Validar_correo_existente(correo_responsable)

        if validacion_correo:
            self.DB.Tarea_Usuario(correo_responsable)
        else:
            print("El correo no existe")

    
    def Terminar_tarea(self, titulo):
        self.DB.Terminar_tarea(titulo)
        self.notificacidor.notificar_Tarea_Terminada(titulo)
        


