from abc import ABC, abstractclassmethod

#Definimos la clase abstracta del usuario 
class Usuario_Base(ABC):
    #Constructor de la clase Usuario
    def __init__(self, nombre, identificacion, correo_electronico, contraseña):
        self.nombre = nombre
        self.identificacion = identificacion
        self.correo_electronico=correo_electronico
        self.contraseña=contraseña

    
class Usuario(Usuario_Base):
    def __str__(self):
        print("Nombre: ", self.nombre)
        print("Identificacion: ", self.identificacion)
        print("Correo Electronico: ", self.correo_electronico)
