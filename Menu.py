from Usuarios import*
from gestor import*
from tareas import*
from Correo import*

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

            elif opcion == 2:
                subopcion = input("1.Agregar Tarea\n2.Eliminar Tarea\n3.Actualizar Tarea\n4.Listar Tareas\nDigite una opción: ")
                if subopcion.isdigit():
                    subopcion = int(subopcion)
                    if subopcion == 1:
                        # Agregar Tarea
                        titulo = input("Digite el título de la tarea: ")
                        descripcion = input("Digite la descripción de la tarea: ")
                        fecha_limite = input("Digite la fecha límite de la tarea (formato YYYY-MM-DD): ")
                        responsable_correo = input("Digite el nombre del usuario responsable: ")

                        # Buscar el usuario responsable en la lista de usuarios
                        responsable = None
                        for usuario in Gestor_app1.usuarios:
                            if usuario.correo_electronico == responsable_correo:
                                responsable = usuario
                                break

                        if responsable:
                            tarea = Tarea(titulo, descripcion, responsable, fecha_limite)
                            Gestor_app1.Agregar_Tarea(tarea)
                            print("Tarea agregada exitosamente")
                        else:
                            print("Usuario responsable no encontrado")

                    elif subopcion == 2:
                        # Eliminar Tarea
                        titulo_tarea = input("Digite el título de la tarea a eliminar: ")
                        tarea_a_eliminar = None
                        for tarea in Gestor_app1.tareas:
                            if tarea.titulo == titulo_tarea:
                                tarea_a_eliminar = tarea
                                break

                        if tarea_a_eliminar:
                            Gestor_app1.Eliminar_tarea(tarea_a_eliminar)
                            print("Tarea eliminada exitosamente")
                        else:
                            print("Tarea no encontrada")

                    elif subopcion == 3:
                        # Actualizar Tarea
                        titulo_tarea = input("Digite el título de la tarea a actualizar: ")
                        Gestor_app1.Actualizar_tarea(titulo_tarea)

                    elif subopcion == 4:
                        # Listar Tareas
                        Gestor_app1.listar_tareas()  # Asegúrate de tener un método listar_tareas en la clase Gestor_app

                    else:
                        print("Opción no válida")
                else:
                    print("Opción no válida")

                                
        


if __name__ == "__main__":
    main()
