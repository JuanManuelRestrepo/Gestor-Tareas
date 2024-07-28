from BasesdeDatos import DatabaseManager as DB
from abc import ABC, abstractclassmethod


class Login_abstact(ABC):
    def __init__(self):
        self.DB=DB()
    @abstractclassmethod
    def validar_credenciales(self):
        pass
    @abstractclassmethod
    def Crear_usuario(self):
        pass

class Login(Login_abstact):

    def validar_credenciales(self, correo_electronico, contraseña):
        if self.DB.validar_credenciales(correo_electronico, contraseña):
            print("Credenciales correctas")
            return True
        else:
            print("Credenciales invalidas")
            return False

    def Crear_usuario(self, nombre, identificacion,correo, confirmar_contraseña):
        self.DB.Crear_usuario(nombre, identificacion, correo, confirmar_contraseña)
        
    

        
    