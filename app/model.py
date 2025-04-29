import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import openai
from app.abstractions import IProcesadorCorreo
from dotenv import load_dotenv

load_dotenv()

class ProcesadorCorreo(IProcesadorCorreo):

    def __init__(self):
        self.smtp_server = os.getenv("SMTP_SERVER")
        self.smtp_port = int(os.getenv("SMTP_PORT"))
        self.client = openai.Client(api_key=os.getenv("OPEN_API_KEY"))

    def generar_respuesta(self, contenido: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "developer", "content": "Eres un asistente que redacta respuestas profesionales a correos."},
                    {"role": "user", "content": f"Escribe una respuesta al siguiente mensaje:\n\n{contenido}"}
                ],
                max_tokens=200,
                temperature=0.7
            )

            return response.choices[0].message.content
        except Exception as e:
            raise RuntimeError(f"Erro al generar respuesta con OpenAI: {e}")

    def enviar_respuesta(self, asunto: str, contenido: str, destinatario: str):
        try:
            mensaje = MIMEMultipart()
            mensaje['From'] = "APOO grupo 64"
            mensaje['To'] = destinatario
            mensaje['Subject'] = asunto
            mensaje.attach(MIMEText(contenido, 'plain'))

            with smtplib.SMTP(self.smtp_server) as server:
                server.send_message(mensaje)
        except Exception as e:
            raise RuntimeError(f"Error al enviar el correo: {e}")
