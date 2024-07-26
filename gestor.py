from abc import ABC, abstractclassmethod
from Usuarios import*
from tareas import*
from Correo import *
from Notificaciones import *
from BasesdeDatos import DatabaseManager as DB


notificacion=Notificacion()
class Gestor_usuarios_Base(ABC):

    @abstractclassmethod
    def Agregarusuario(self,Usuario):
        pass

    @abstractclassmethod
    def Agregar_Tarea(self,Tarea):
        pass
  
    @abstractclassmethod
    def Eliminar_usuario(self, usuario):
        pass
    @abstractclassmethod
    def Eliminar_tarea(self, Tarea):
        pass
    @abstractclassmethod
    def Actualizar_tarea(self,Tarea):
        pass
    @abstractclassmethod
    def Actualizar_usuario(self, usuario):
        pass
    @abstractclassmethod
    def listar_usuarios(self):
        pass
    @abstractclassmethod
    def listar_tareas(self):
        pass
    @abstractclassmethod
    def Tarea_usuario(self):
        pass
    """
    @abstractclassmethod
    def Terminar_tarea(self):
        pass"""

class Gestor_app(Gestor_usuarios_Base):

    def __init__(self):
        self.notificacidor=notificacion
        self.DB=DB()
        
    def Agregarusuario(self, usuario):
        #comprobamos que el objeto(primer elemento) sea una instancia de la clase Usuario(segundo elemento)
        if not isinstance(usuario,Usuario):
            #raise se utiliza para lanzar excepciones
            raise ValueError(" EL objeto no es una instacia de la clase Usuario")
        usuario_existente=self.DB.validar_usuario(usuario.identificacion)
        if not usuario_existente:
            self.DB.agregar_usuario(usuario.nombre, usuario.identificacion, usuario.correo_electronico)
            print(f"Usuario {usuario.nombre} agregado.")
        else:
             print("Usuario existente")

    def listar_usuarios(self):
        self.DB.listar_usuarios()

    def Actualizar_usuario(self, identificacion): 
        usuario=self.DB.validar_usuario(identificacion)
        if usuario:
            nuevo_nombre=input("Digite el nuevo nombre")
            nuevo_correo=input("Digite el nuevo correo")
            self.DB.Actualizar_usuario(identificacion,nuevo_nombre, nuevo_correo)
        else:
            print("Usuario no encontrado")

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

    def Eliminar_usuario(self,correo):
        usuario=self.DB.Validar_correo_existente(correo)
        if usuario:
            self.DB.eliminar_usuario(correo)
            print(f"Usuario {correo} eliminado")
        else:
            print("Usuario no encontrado")
    
    def Eliminar_tarea(self,titulo):
        validacion=self.DB.validar_tarea(titulo)
        if validacion:
            self.DB.eliminar_tarea(titulo)
            print(f"Tarea {titulo} eliminada")
        else:
            print("Tarea no encontrada")
            

    def Actualizar_tarea(self, tarea_titulo): 
        tarea=self.DB.validar_tarea(tarea_titulo)
        if tarea:
            nuevo_titulo=input("Digite el nuevo nombre")
            nueva_descripcion=input("Digite el nuevo correo")
            nueva_fecha_limite = datetime.strptime(nueva_fecha_limite, "%Y-%m-%d")
            responsable_correo=input("Digite el correo del responsable")
            self.DB.Actualizar_usuario(tarea_titulo, nuevo_titulo, nueva_descripcion, nueva_fecha_limite, responsable_correo)
            self.notificacidor.correo(responsable_correo)
            print("Tarea no encontrada")

    def listar_tareas(self):
       self.DB.listar_tareas()

    def Tarea_usuario(self, correo_responsable):
        validacion_correo=self.DB.Validar_correo_existente()

        if validacion_correo:
            self.DB.Tarea_Usuario(correo_responsable)
        else:
            print("El correo no existe")

        
"""
    def Terminar_tarea(self):
        tarea_terminar = input("Ingrese el titulo de la tarea a terminar: ")
        tarea_notificar=None
        for tarea in self.tareas:
            if tarea.titulo == tarea_terminar:
                tarea.estado = "Terminada"
                print(f"Tarea {tarea.titulo} terminada")
                tarea_notificar=tarea
                self.notificacidor.notificar_Tarea_Terminada(tarea_notificar)
"""


