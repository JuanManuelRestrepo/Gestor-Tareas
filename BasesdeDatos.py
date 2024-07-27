import sqlite3
from datetime import datetime
class DatabaseManager:
    def __init__(self, db_name='gestor.db'):
        # Conecta a la base de datos especificada por `db_name`.
        # Si el archivo de la base de datos no existe, SQLite lo creará.
        self.connection = sqlite3.connect(db_name)
        # Crea un cursor para interactuar con la base de datos.
        self.cursor_DB = self.connection.cursor()
        # Llama al método para crear las tablas en la base de datos.
        self.create_tables()

    def create_tables(self):
        # Crea la tabla 'USERS' si no existe.
        # Esta tabla almacenará la información de los usuarios.
        self.cursor_DB.execute('''CREATE TABLE IF NOT EXISTS USERS (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nombre TEXT NOT NULL,
                                    identificacion TEXT NOT NULL UNIQUE,
                                    correo_electronico TEXT NOT NULL UNIQUE
                                )''')

        # Crea la tabla 'tareas' si no existe.
        # Esta tabla almacenará la información de las tareas.
        # La columna 'responsable_id' es una clave foránea que referencia al campo 'id' de la tabla 'USERS'.
        self.cursor_DB.execute('''CREATE TABLE IF NOT EXISTS tareas (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                titulo TEXT NOT NULL,
                                descripcion TEXT,
                                fecha_limite DATE,
                                estado TEXT,
                                responsable_id INTEGER,
                                FOREIGN KEY (responsable_id) REFERENCES USERS (id)
                              )''')
        
        # Guarda los cambios realizados en la base de datos.
        # Esto asegura que las tablas se creen y cualquier otro cambio se persista.
        self.connection.commit()
    
    def agregar_usuario(self, nombre, identificacion, correo_electronico):
        try:
            # Inserte los datos en las columnas
            self.cursor_DB.execute('''INSERT INTO USERS (nombre, identificacion, correo_electronico)
                                VALUES (?, ?, ?)''', (nombre, identificacion, correo_electronico))
            # Los valores a insertar en la base de datos se pasan como una tupla (nombre, identificacion, correo_electronico)
            
            self.connection.commit()  # Hace un commit de todas las operaciones que se han hecho a la base de datos a través de esa conexión
            print(f"Usuario {nombre} agregado.")

        except sqlite3.IntegrityError:
            # Este bloque se ejecutará si ocurre un error de integridad, como intentar insertar un usuario con una identificación ya existente
            print("Usuario existente")

    def validar_usuario(self, identificacion):
        try:
            self.cursor_DB.execute('''SELECT 1 FROM USERS WHERE identificacion=?''', (identificacion,))
            resultado = self.cursor_DB.fetchone()
            return resultado is not None
        except sqlite3.DatabaseError as e:
            print(f"Error al verificar el usuario: {e}")
            return False

    def Validar_correo_existente(self, correo_electronico):
        try:
            # Ejecutar la consulta SQL para buscar el correo electrónico
            self.cursor_DB.execute('''SELECT 1 FROM USERS WHERE correo_electronico = ?''', (correo_electronico,))
            
            # fetchone() recupera una única fila del resultado de la consulta
            resultado = self.cursor_DB.fetchone()
            
            # Si fetchone() devuelve una fila, el correo electrónico existe
            if resultado:
                return True
            else:
                return False
    
        except sqlite3.DatabaseError as e:
            print(f"Error al verificar el correo electrónico: {e}")
            return False
        
    def eliminar_usuario(self, correo):
        id_resp = self.Obtener_id_responsable(correo)
            
        if id_resp is None:
            print(f"No se encontró el usuario con correo {correo}.")
            return
        
        try:
            # Primero, actualizar las tareas asignadas al usuario para establecer responsable_id en NULL
            self.cursor_DB.execute('''UPDATE tareas SET responsable_id=NULL WHERE responsable_id=?''', (id_resp,))

            
            # Luego, eliminar al usuario
            self.cursor_DB.execute('''DELETE FROM USERS WHERE id=?''', (id_resp,))
            
            # Confirmar los cambios en la base de datos
            self.connection.commit()
            
            print(f"Usuario con correo {correo} eliminado y tareas actualizadas.")
            
        
        except sqlite3.OperationalError as e:
            print(f"Error operativo al eliminar el usuario: {e}. La base de datos puede estar bloqueada.")
        except sqlite3.DatabaseError as e:
            print(f"Error al eliminar el usuario: {e}.")

    def listar_usuarios(self):
        # Ejecuta una consulta SQL para seleccionar el nombre y el correo electrónico de todos los usuarios.
        self.cursor_DB.execute('''SELECT nombre, correo_electronico FROM USERS''')

        # Recupera todos los resultados de la consulta ejecutada.
        usuarios = self.cursor_DB.fetchall()

        # Itera sobre cada usuario en la lista de resultados.
        for usuario in usuarios:
            # Imprime el nombre y el correo electrónico de cada usuario.
            print(f"Nombre: {usuario[0]} || Correo: {usuario[1]}")
    
    def Actualizar_usuario(self, id_resp, nuevo_nombre, nuevo_correo):
        try:
            # Ejecutar la consulta SQL para actualizar la información del usuario en la base de datos
            # La consulta actualiza el nombre y el correo electrónico del usuario basado en la identificación proporcionada
            self.cursor_DB.execute('''UPDATE USERS SET nombre=?, correo_electronico=? WHERE id=?''', 
                                (nuevo_nombre, nuevo_correo, id_resp))
            
            # Confirmar los cambios en la base de datos
            # Los cambios realizados por la consulta SQL se guardan permanentemente en la base de datos
            self.connection.commit()
            
            # Mensaje indicando que la actualización fue exitosa
            print("Usuario actualizado correctamente.")
    
        except sqlite3.IntegrityError:
            # Captura y maneja errores relacionados con la integridad de la base de datos, como claves duplicadas
            # Imprime un mensaje si ocurre un error al actualizar el usuario
            print("Error de integridad. Verifica los datos proporcionados.")

    def Obtener_id_responsable(self, correo_electronico):
        # Ejecutamos una consulta que trae el id del usuario por medio del correo electrónico
        self.cursor_DB.execute(
            '''SELECT id FROM USERS WHERE correo_electronico=?''',  # Consulta SQL que selecciona el id del usuario basado en el correo electrónico
            (correo_electronico,)  # Parámetro para reemplazar el marcador de posición ? en la consulta
        )

        # Recuperamos una sola fila del resultado de la consulta
        resultado = self.cursor_DB.fetchone()

        # Devolvemos el id encontrado si existe, de lo contrario devolvemos None
        if resultado:
            return resultado[0]  # Devuelve el ID
        return None
    
    def agregar_tarea(self, titulo, descripcion, fecha_limite, estado, responsable_correo):
        try:
            # Obtener el ID del responsable basándose en el correo electrónico proporcionado
            id_responsable = self.Obtener_id_responsable(responsable_correo)
            
            # Insertar una nueva tarea en la base de datos
            self.cursor_DB.execute('''INSERT INTO tareas (titulo, descripcion, fecha_limite, estado, responsable_id)
                                VALUES (?, ?, ?, ?, ?)''', (titulo, descripcion, fecha_limite, estado, id_responsable))
            
            # Confirmar los cambios en la base de datos
            self.connection.commit()
            print(f"Tarea {titulo} agregada.")
        except sqlite3.IntegrityError:
            # Captura el error de integridad si ya existe una tarea con el mismo título
            print("Tarea existente")

    def validar_tarea(self, titulo):
        # Ejecuta una consulta para verificar si existe una tarea con el título proporcionado
        self.cursor_DB.execute('''SELECT 1 FROM tareas WHERE titulo=?''',(titulo,))
        
        # Recupera una única fila del resultado de la consulta
        # Si la consulta devuelve una fila, significa que existe una tarea con el título
        return self.cursor_DB.fetchone() is not None

    def listar_tareas(self):
        # Ejecuta una consulta para seleccionar todas las tareas
        self.cursor_DB.execute('''SELECT titulo, descripcion, fecha_limite, estado FROM tareas''')
        
        # Recupera todas las filas del resultado de la consulta
        tareas = self.cursor_DB.fetchall()
        
        # Itera sobre las tareas recuperadas y las imprime
        for tarea in tareas:
            try:
                # Suponiendo que fecha_limite en la base de datos es en formato "YYYY-MM-DD HH:MM:SS"
                fecha_limite_str = datetime.strptime(tarea[2], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")
                print(f"Título: {tarea[0]}")
                print(f"Descripción: {tarea[1]}")
                print(f"Fecha límite: {fecha_limite_str}")
                print(f"Estado: {tarea[3]}")
                print("-" * 30)
            except ValueError as e:
                # Manejo de errores si el formato de fecha es incorrecto
                print(f"Error al convertir la fecha: {e}")
                print(f"Tarea con fecha inválida: {tarea}")

    def Actualizar_tarea(self, titulo, nuevo_titulo=None, nueva_descripcion=None, nueva_fecha=None, correo_responsable=None):
        tarea_validar=self.validar_tarea(titulo)
        if tarea_validar:
            try:
                # Verificar y obtener el ID del responsable si se proporciona un correo
                if correo_responsable:
                    id_responsable = self.Obtener_id_responsable(correo_responsable)
                    if not id_responsable:
                        print("Responsable con correo electrónico no encontrado.")
                        return
                    else:
                        pass #abierta a implementacion
                # Construir la consulta SQL y valores basados en los campos proporcionados
                if nuevo_titulo and nueva_descripcion and nueva_fecha and id_responsable:
                    consulta = '''UPDATE tareas 
                                SET titulo=?, descripcion=?, fecha_limite=?, responsable_id=? 
                                WHERE titulo=?'''
                    valores = (nuevo_titulo, nueva_descripcion, nueva_fecha, id_responsable, titulo)
                elif nuevo_titulo and nueva_descripcion and nueva_fecha:
                    consulta = '''UPDATE tareas 
                                SET titulo=?, descripcion=?, fecha_limite=? 
                                WHERE titulo=?'''
                    valores = (nuevo_titulo, nueva_descripcion, nueva_fecha, titulo)
                elif nuevo_titulo and nueva_descripcion:
                    consulta = '''UPDATE tareas 
                                SET titulo=?, descripcion=? 
                                WHERE titulo=?'''
                    valores = (nuevo_titulo, nueva_descripcion, titulo)
                elif nuevo_titulo:
                    consulta = '''UPDATE tareas 
                                SET titulo=? 
                                WHERE titulo=?'''
                    valores = (nuevo_titulo, titulo)
                else:
                    print("No se especificaron cambios para actualizar.")
                    return
                
                # Ejecutar la consulta SQL con los valores proporcionados
                self.cursor_DB.execute(consulta, valores)
                self.connection.commit()
                
                print("Tarea actualizada correctamente.")
            except sqlite3.IntegrityError:
                # Captura el error de integridad si se produce un problema con los datos proporcionados
                print("Error de integridad. Verifica los datos proporcionados.")
            except sqlite3.DatabaseError as e:
                # Captura cualquier otro error de base de datos y lo imprime
                print(f"Error al actualizar la tarea: {e}")

        else:
            print("Tarea no encontrada")

    def Tarea_Usuario(self, correo_electronico):
        try:
            #Obtenemos el id del responsable con el correo 
            id_responsable=self.Obtener_id_responsable(correo_electronico)
            #traemos en la consukta las tareas de la tbla tareas donde el id_responsable, sea el mismo que el traimos anteriormente
            self.cursor_DB.execute(''' SELECT titulo, descripcion, fecha_limite, estado
                                        FROM tareas
                                        WHERE responsable_id = ?
                                        '''), (id_responsable)
            tareas = self.cursor_DB.fetchall()

            # Imprimir los detalles de cada tarea
            for tarea in tareas:
                fecha_limite_str = datetime.strptime(tarea[2], "%Y-%m-%d").strftime("%Y-%m-%d")
                print(f"Título: {tarea[0]}, Descripción: {tarea[1]}, Fecha límite: {fecha_limite_str}, Estado: {tarea[3]}")

        except sqlite3.DatabaseError as e:
            print(f"Error al obtener las tareas del usuario: {e}")

    def eliminar_tarea(self, titulo):
        validacion=self.validar_tarea(titulo)
        if validacion:
            try:
                validacion=self.validar_tarea(titulo)
                if validacion:
                    # Eliminar la tarea con el título especificado
                    self.cursor_DB.execute('''DELETE FROM tareas WHERE titulo=?''' ,(titulo,))
                    self.connection.commit()
                    print("Tarea eliminada correctamente.")
            except sqlite3.DatabaseError as e:
                print(f"Error al eliminar la tarea: {e}")

        else:
            print("No se encontró la tarea a eliminar")

    def Terminar_tarea(self,titulo):
        validacion=self.validar_tarea(titulo)
        if validacion:
            try:
                # Actualizar el estado de la tarea a "Terminada"
                self.cursor_DB.execute('''UPDATE tareas SET estado=? WHERE titulo=?''', ("Terminada", titulo,))
                self.connection.commit()
                print("Tarea terminada exitosamente")
            except sqlite3.DatabaseError as e:
                print(f"Error al terminar la tarea: {e}")

    def notificacion_cambio_tarea(self, titulo):
        validacion=self.validar_tarea(titulo)
        if validacion:
            try:
                self.cursor_DB.execute('''SELECT descripcion,fecha_limite,estado, responsable_id FROM tareas WHERE titulo=?''', (titulo,))
                tarea = self.cursor_DB.fetchone()
                if tarea:
                    descripcion = tarea[0]
                    fecha_limite = tarea[1]
                    estado = tarea[2]
                    responsable_id = tarea[3]
               
                    self.cursor_DB.execute('''SELECT correo_electronico FROM USERS WHERE id=? ''', (responsable_id,))
                    correo = self.cursor_DB.fetchone()
                    if correo:
                        correo_electronico=correo[0]
                        return titulo, descripcion,fecha_limite,estado,correo_electronico
                    else:
                        print("No se encontró el correo del responsable.")
                else:
                    print("No se encontró la tarea.")
        
            except sqlite3.DatabaseError as e:
                print(f"Error al obtener la tarea: {e}")
        else:
            print("No se encontró la tarea.")

    def close(self):
        # Cierra la conexión a la base de datos
        self.connection.close()

        


