from abc import ABC, abstractclassmethod
from Usuarios import*
from tareas import*
from Correo import *
from Notificaciones import *

notificacion=Notificacion()
class Gestor_usuarios_Base(ABC):

    @abstractclassmethod
    def Agregarusuario(self,Usuario):
        pass
    @abstractclassmethod
    def Validar_usuario(self):
        pass
    @abstractclassmethod
    def Agregar_Tarea(self,Tarea):
        pass
    @abstractclassmethod
    def Validar_tarea(self):
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
    @abstractclassmethod
    def Terminar_tarea(self):
        pass
class Gestor_app(Gestor_usuarios_Base):

    def __init__(self):
        #definimos dos listas donde se almacenaran los usuarios y las tareas
        self.usuarios = []
        self.tareas = []
        self.tarea_usuario=[]
        self.notificacidor=notificacion
        
    def Agregarusuario(self, usuario):
        #comprobamos que el objeto(primer elemento) sea una instancia de la clase Usuario(segundo elemento)
        if not isinstance(usuario,Usuario):
            #raise se utiliza para lanzar excepciones
            raise ValueError(" EL objeto no es una instacia de la clase Usuario")
        usuario_existente=self.Validar_usuario(usuario.identificacion,usuario.correo_electronico)
        if not usuario_existente:
            self.usuarios.append(usuario)
            print(f"Usuario {usuario.nombre} agregado.")
        else:
             print("Usuario existente")
    
    def Validar_usuario(self, identificacion, correo_electronico):
            for usuario in self.usuarios:
                if usuario.identificacion == identificacion or usuario.correo_electronico == correo_electronico:
                    return True
            return False
    def Agregar_Tarea(self, tarea):
        #misma comprobancion anterior
        if not isinstance(tarea, Tarea):
            raise ValueError(" EL objeto no es una instacia de la clase Tarea")
        tarea_existente=self.Validar_tarea(tarea.titulo)
        if tarea_existente==False:
            self.tareas.append(tarea)
            notificacion.notificar_Nueva_Tarea(tarea)

    def Validar_tarea(self, titulo):
        tarea_existente=False
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                print("Tarea ya existente")
                tarea_existente=True
        return tarea_existente

    def Eliminar_usuario(self,identificacion):
        usuario_eliminar=None
        for usuario in self.usuarios:
            if usuario.identificacion ==identificacion:
                usuario_eliminar=usuario
                break

        if usuario_eliminar:
            self.usuarios.remove(usuario_eliminar)
            print(f"Usuario {usuario_eliminar.nombre} eliminado.")
        else:
            raise ValueError("El usuario no existe")
    
    def Eliminar_tarea(self,tarea):
        if tarea not  in self.usuarios:
            raise ValueError("El usuario no existe")
        self.tareas.remove(tarea)
        print(f"usuario {tarea.titulo} eliminado")

    def Actualizar_tarea(self, tarea_titulo): 
        tarea_actualizar=None
        for tarea in self.tareas:
            if tarea.titulo ==tarea_titulo:
                tarea_actualizar=tarea
                break

        if tarea_actualizar:
            nuevo_titulo = input("Ingrese el nuevo título de la tarea: ")
            nueva_descripcion = input("Ingrese la nueva descripción de la tarea: ")
            nueva_fecha_limite = input("Ingrese la nueva fecha límite (formato YYYY-MM-DD): ")
            nuevo_estado = input("Ingrese el nuevo estado de la tarea: ")
            # Convertir la nueva fecha límite a datetime
            try:
                nueva_fecha_limite = datetime.strptime(nueva_fecha_limite, "%Y-%m-%d")
            except ValueError:
                print("Formato de fecha incorrecto. Utilice YYYY-MM-DD.")
                return
            tarea.titulo = nuevo_titulo
            tarea.descripcion = nueva_descripcion
            tarea.fecha_limite = nueva_fecha_limite
            tarea.estado = nuevo_estado
            print("Tarea Actualizada")
            self.notificacidor.notificar_Tarea_Cambios(tarea_actualizar)

        else:
            raise ValueError(f"la tarea {tarea_titulo} no existe" )

    def Actualizar_usuario(self, identificacion): 

        usuario_actualizar=None
        for usuario in self.usuarios:
            if usuario.identificacion ==identificacion:
                usuario_actualizar=usuario
                break
        if usuario_actualizar:
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            nueva_correo = input("Ingrese el nuevo correo: ")
            usuario.nombre=nuevo_nombre
            usuario.correo_electronico=nueva_correo
            print("Usuario Actualizado")
    
        else:
            raise ValueError("El usuario no existe")
   
    def listar_usuarios(self):
        print("Listando todos los usuarios Creados")
        for usuario in self.usuarios:
            print(f"Nombre: {usuario.nombre} \t correo: {usuario.correo_electronico}")

    def listar_tareas(self):
        print("Listando todos los usuarios Creados")
        for tarea in self.tareas:
            print(f"Titulo: {tarea.titulo} \t Responsable: {tarea.responsable.nombre}")  

    def Tarea_usuario(self, usuario):
        if not isinstance(usuario, Usuario):
            raise ValueError("El objeto no es una instacia de la clase Usuario")
        for tarea in self.tareas:
            if tarea.responsable == usuario:
                self.tarea_usuario.append(tarea)
        if not self.tarea_usuario:
            print(f"No hay tareas asignadas a {usuario.nombre}.")
        else:
            print(f"Tareas asignadas a {usuario.nombre}:")
            for tarea in self.tarea_usuario:
                print(tarea)

    def Terminar_tarea(self):
        tarea_terminar = input("Ingrese el titulo de la tarea a terminar: ")
        tarea_notificar=None
        for tarea in self.tareas:
            if tarea.titulo == tarea_terminar:
                tarea.estado = "Terminada"
                print(f"Tarea {tarea.titulo} terminada")
                tarea_notificar=tarea
                self.notificacidor.notificar_Tarea_Terminada(tarea_notificar)




