from Usuarios import*
from tareas import*
from Correo import*
from Login  import *
from gestor_usuarios import *
from gestor_tareas import *

Gestor_app1=Gestor_Tareas()
Login_usuario=Login()
Gestor_usuario=Gestor_usuarios()

def Iniciar_sesion():
        correo_electronico=input("Ingrese el correo electronico")
        contraseña=input("Ingrese la contraseña")
        if Login_usuario.validar_credenciales(correo_electronico, contraseña):
            Menu()
        else: 
            print("Credenciales invalidas")

def Crear_usuario():
        nombre=input("Digite el nombre del usuario: ")
        identificacion=input("Digite el numero de identificacion: ")
        correo=input("Digite el correo: ")
        contraseña= input("Digite una contraseña")
        confirmar_contraseña=input("Digite una contraseña")
        if contraseña== confirmar_contraseña:
            Login_usuario.Crear_usuario(nombre, identificacion,correo, confirmar_contraseña)

def main():
    print("bienvenido")
    while True:
        opcion_principal=int(input("1. Iniciar sesion\n2.Crear usuario"))
        if opcion_principal==1:
            Iniciar_sesion()
        elif opcion_principal==2:
            Crear_usuario()
                
def Menu():
    while True:
        opcion=input("1.Usuarios\n2.Tareas\nDigite una opcion")
        if opcion.isdigit():
            opcion=int(opcion)
            if opcion==1:
                subopcion=input("2.Elimianr Usuario\n3.Actualizar Usuario\n4.Listar Usuarios\nDigite una opcion: ")
                if subopcion.isdigit():
                    subopcion=int(subopcion)
                    if subopcion ==2:
                        usuario_eliminar=input("Digite el correo del usuario a eliminar")
                        Gestor_usuario.Eliminar_usuario(usuario_eliminar)

                    elif subopcion==3:
                        usuario_actualizar=input("Digite el correo del usuario a actualizar: ")
                        Gestor_usuario.Actualizar_usuario(usuario_actualizar)

                    elif subopcion==4:
                        Gestor_usuario.listar_usuarios()
                        
                else: 
                    print("Opcion no valida")

            elif opcion == 2:
                subopcion = input("1.Agregar Tarea\n2.Eliminar Tarea\n3.Actualizar Tarea\n4.Listar Tareas\n5.Terminar Tarea\nDigite una opción: ")
                if subopcion.isdigit():
                    subopcion = int(subopcion)
                    if subopcion == 1:
                            # Agregar Tarea
                            titulo = input("Digite el título de la tarea: ")
                            descripcion = input("Digite la descripción de la tarea: ")
                            fecha_limite = input("Digite la fecha límite de la tarea (formato YYYY-MM-DD): ")
                            responsable_correo = input("Digite el correo del usuario responsable: ")
                            tarea = Tarea(titulo, descripcion, fecha_limite, responsable_correo)
                            Gestor_app1.Agregar_Tarea(tarea)
                        
                    elif subopcion == 2:
                        # Eliminar Tarea
                        titulo_tarea = input("Digite el título de la tarea a eliminar: ")
                        Gestor_app1.Eliminar_tarea(titulo_tarea)

                    elif subopcion == 3:
                        # Actualizar Tarea
                        titulo_tarea = input("Digite el título de la tarea a actualizar: ")
                        Gestor_app1.Actualizar_tarea(titulo_tarea)
                        

                    elif subopcion == 4:
                        # Listar Tareas
                        Gestor_app1.listar_tareas()  # Asegúrate de tener un método listar_tareas en la clase Gestor_app
                    elif subopcion==5:
                        # Terminar Tarea
                        titulo_tarea = input("Digite el título de la tarea a terminar: ")
                        Gestor_app1.Terminar_tarea(titulo_tarea)

                    elif subopcion ==6:
                        correo_responsable=input("Digite el correo del usuario")
                        Gestor_app1.Tarea_usuario(correo_responsable)
                        


                    else:
                        print("Opción no válida")
                else:
                    print("Opción no válida")

                                
        


if __name__ == "__main__":
    main()
