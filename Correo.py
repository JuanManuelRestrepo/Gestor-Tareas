import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from abc import ABC,abstractclassmethod

class Correo_base(ABC):
    def __init__(self, remitente, contraseña_aplicacion):
        self.remitente=remitente
        self.contraseña=contraseña_aplicacion
        self.servidor_smtp='smtp.gmail.com'
        self.puerto=587

    @abstractclassmethod
    def enviar_correo(self):
        pass

class Correo_gmail(Correo_base):
    def __init__(self, remitente, contraseña):
        self.remitente=remitente
        self.contraseña=contraseña
        self.servidor_smtp='smtp.gmail.com'
        self.puerto=587

    def enviar_correo(self, destinatario, asunto,cuerpo):
        # Crear el mensaje
        mensaje = MIMEMultipart() #creamos un objeto del modulo importado
        mensaje['From'] = self.remitente
        mensaje['To'] = destinatario
        mensaje['Subject'] = asunto
        mensaje.attach(MIMEText(cuerpo, 'plain'))

        try:
            # Conectarse al servidor SMTP y enviar el correo
            servidor=smtplib.SMTP(self.servidor_smtp, self.puerto)
            servidor.starttls() #habilitamos la conexion segura 
            servidor.login(self.remitente, self.contraseña) #accedemos a la cuenta del remitente
            texto=mensaje.as_string()
            servidor.sendmail(self.remitente, destinatario, texto) #enviamos el
            servidor.quit()  # Cerramos la conexión
            print("Correo enviado exitosamente")

        except Exception as e:
            print(f"Error al enviar el correo: {e}")

    