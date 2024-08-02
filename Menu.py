from Usuarios import*
from Correo import*
from Login import *
from tareas import*
from gestor_usuarios import *
from gestor_tareas import *

Gestor_app1 = Gestor_Tareas()
Login_usuario = Login()
Gestor_usuario = Gestor_usuarios()

def Iniciar_sesion():
    correo_electronico = input("Ingrese el correo electronico: ")
    contraseña = input("Ingrese la contraseña: ")
    if Login_usuario.validar_credenciales(correo_electronico, contraseña):
        print("Inicio de sesión exitoso.")
        menu_principal()
    else: 
        print("Credenciales inválidas")

def Crear_usuario():
    nombre = input("Digite el nombre del usuario: ")
    identificacion = input("Digite el número de identificación: ")
    correo = input("Digite el correo: ")
    contraseña = input("Digite una contraseña: ")
    confirmar_contraseña = input("Confirme la contraseña: ")
    if contraseña == confirmar_contraseña:
        Login_usuario.Crear_usuario(nombre, identificacion, correo, confirmar_contraseña)
    else:
        print("Las contraseñas no coinciden.")

def login():
    print("Bienvenido")
    while True:
        try:
            opcion_principal = int(input("1. Iniciar sesión\n2. Crear usuario\n3. Salir\nDigite un valor: "))
            if opcion_principal == 1:
                Iniciar_sesion()
            elif opcion_principal == 2:
                Crear_usuario()
            elif opcion_principal == 3:
                break
        except ValueError:
            print("Digite un valor válido")

def menu_principal():
    while True:
        try:
            opcion = int(input("1. Usuarios\n2. Tareas\n3. Configuraciones\n4. Salir\nDigite una opción: "))
            if opcion == 1:
                menu_usuarios()
            elif opcion == 2:
                menu_tareas()
            elif opcion == 3:
                Menu_configuraciones()
            elif opcion ==4:
                break
        except ValueError:
            print("Opción no válida")

def menu_usuarios():
    while True:
        try:
            subopcion = int(input("1. Eliminar Usuario\n2. Actualizar Usuario\n3. Listar Usuarios\n4. Salir\nDigite una opción: "))
            if subopcion == 1:
                usuario_eliminar = input("Digite el correo del usuario a eliminar: ")
                Gestor_usuario.Eliminar_usuario(usuario_eliminar)
            elif subopcion == 2:
                usuario_actualizar = input("Digite el correo del usuario a actualizar: ")
                Gestor_usuario.Actualizar_usuario(usuario_actualizar)
            elif subopcion == 3:
                Gestor_usuario.listar_usuarios()
            elif subopcion == 4:
                break
        except ValueError:
            print("Opción no válida")

def menu_tareas():
    while True:
        try:
            subopcion = int(input("1. Agregar Tarea\n2. Eliminar Tarea\n3. Actualizar Tarea\n4. Listar Tareas\n5. Terminar Tarea\n6. Filtro Tarea por usuario\n7. Salir\nDigite una opción: "))
            if subopcion == 1:
                titulo = input("Digite el título de la tarea: ")
                descripcion = input("Digite la descripción de la tarea: ")
                fecha_limite = input("Digite la fecha límite de la tarea (formato YYYY-MM-DD): ")
                responsable_correo = input("Digite el correo del usuario responsable: ")
                tarea = Tarea(titulo, descripcion, fecha_limite, responsable_correo)
                Gestor_app1.Agregar_Tarea(tarea)
            elif subopcion == 2:
                titulo_tarea = input("Digite el título de la tarea a eliminar: ")
                Gestor_app1.Eliminar_tarea(titulo_tarea)
            elif subopcion == 3:
                titulo_tarea = input("Digite el título de la tarea a actualizar: ")
                Gestor_app1.Actualizar_tarea(titulo_tarea)
            elif subopcion == 4:
                Gestor_app1.listar_tareas()
            elif subopcion == 5:
                titulo_tarea = input("Digite el título de la tarea a terminar: ")
                Gestor_app1.Terminar_tarea(titulo_tarea)
            elif subopcion == 6:
                correo_responsable = input("Digite el correo del usuario: ")
                Gestor_app1.Tarea_usuario(correo_responsable)
            elif subopcion == 7:
                break
        except ValueError:
            print("Opción no válida")

def Menu_configuraciones():
    while True:
            subopcion = int(input("1. Cambiar contraseña\n2.Salir"))
            if subopcion == 1:
                correo = input("Digite el correo del usuario: ")
                contraseña = input("Digite la contraseña actual: ")
                nueva_contraseña = input("Digite la nueva contraseña: ")
                comprobar_contraseña= input("Digite la contraseña de nuevo")
                if comprobar_contraseña == contraseña:
                    print("Contraseña igual a la anterior")
                else:
                    Gestor_usuario.cambio_de_contraseña(correo, nueva_contraseña)
            elif subopcion==2:
                break

if __name__ == "__main__":
    login()
