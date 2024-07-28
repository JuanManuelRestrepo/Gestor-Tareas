from BasesdeDatos import DatabaseManager as DB
from Usuarios import*
from abc import ABC, abstractclassmethod

class Gestor_base(ABC):
    def __init__(self):
        self.DB=DB()
    
    @abstractclassmethod
    def Eliminar_usuario(self, usuario):
        pass
    
    @abstractclassmethod
    def Actualizar_usuario(self, usuario):
        pass
    @abstractclassmethod
    def listar_usuarios(self):
        pass

class Gestor_usuarios(Gestor_base):
        def listar_usuarios(self):
            self.DB.listar_usuarios()

        def Actualizar_usuario(self, correo): 
            id_resp=self.DB.Obtener_id_responsable(correo)
            if id_resp:
                nuevo_nombre=input("Digite el nuevo nombre")
                nuevo_correo=input("Digite el nuevo correo")
                self.DB.Actualizar_usuario(id_resp,nuevo_nombre, nuevo_correo)
            else:
                print("Usuario no encontrado")

        def Eliminar_usuario(self,correo):
            usuario=self.DB.Validar_correo_existente(correo)
            if usuario:
                self.DB.eliminar_usuario(correo)
                print(f"Usuario {correo} eliminado")
            else:
                print("Usuario no encontrado")
