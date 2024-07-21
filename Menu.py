from Usuarios import*
from gestor import*
from tareas import*

def main():
    Gestor_app1=Gestor_app()
    while True:

        opcion=input("1.Usuarios\n2.Tareas\nDigite una opcion")

        if opcion.isdigit():
            opcion=int(opcion)
            if opcion==1:
                subopcion=input("1.Agregar Usuario \n2.Elimianr Usuario\n3.Actualizar Usuario\n4.Listar Usuarios\nDigite una opcion: ")
                if subopcion.isdigit():
                    subopcion=int(subopcion)
                    if subopcion==1:
                        nombre=input("Digite el nombre del usuario: ")
                        identificacion=input("Digite el numero de identificacion: ")
                        correo=input("Digite el correo: ")
                        usuario=nombre
                        usuario=Usuario(nombre, identificacion,correo)
                        Gestor_app1.Agregarusuario(usuario)
                        print("Usuario creado exitosamente")
                    elif subopcion ==2:
                        usuario_eliminar=input("Digite la identificacion del usuario a eliminar")
                        Gestor_app1.Eliminar_usuario(usuario_eliminar)

                    elif subopcion==3:
                        usuario_actualizar=input("Digite la identificacion del usuario a actualizar: ")
                        Gestor_app1.Actualizar_usuario(usuario_actualizar)

                    elif subopcion==4:
                        Gestor_app1.listar_usuarios()
                        
                else: 
                    print("Opcion no valida")
        
        else: 
            print("Opcion no valida")



if __name__ == "__main__":
    main()