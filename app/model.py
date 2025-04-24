from app.abstractions import IProcesadorCorreo


class ProcesadorCorreo(IProcesadorCorreo):

    def generar_respuesta(self, contenido: str) -> str:
        pass

    def enviar_respuesta(self, asunto: str, contenido: str, destinatario: str):
        pass