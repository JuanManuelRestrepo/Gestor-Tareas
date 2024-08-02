from datetime import datetime

class Tarea():
    #Metodo constructopr, con sus atributos
    def __init__(self, titulo, descripcion, fecha_limite, responsable_correo):
        try:
            self.fecha_limite = datetime.strptime(fecha_limite, "%Y-%m-%d")
        except ValueError as e:
            print(f"Error al convertir la fecha: {e}")
            # Maneja el error o asigna un valor por defecto
            self.fecha_limite = None
        self.titulo = titulo
        self.descripcion = descripcion
        self.responsable_correo = responsable_correo
        self.estado="Pendiente"