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
                    elif subopcion ==2:
                        usuario_eliminar=input("Digite el correo del usuario a eliminar")
                        Gestor_app1.Eliminar_usuario(usuario_eliminar)

                    elif subopcion==3:
                        usuario_actualizar=input("Digite la identificacion del usuario a actualizar: ")
                        Gestor_app1.Actualizar_usuario(usuario_actualizar)

                    elif subopcion==4:
                        Gestor_app1.listar_usuarios()
                        
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
                        Gestor_app1.Terminar_tarea (titulo_tarea)

                    elif subopcion ==6:
                        correo_responsable=input("Digite el correo del usuario")
                        Gestor_app1.Tarea_usuario(correo_responsable)
                        


                    else:
                        print("Opción no válida")
                else:
                    print("Opción no válida")

                                
        


if __name__ == "__main__":
    main()
