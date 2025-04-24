from abc import ABC, abstractmethod

class IProcesadorCorreo(ABC):

    @abstractmethod
    def generar_respuesta(self, contenido: str) -> str:
        ...

    @abstractmethod
    def enviar_respuesta(self, asunto: str, contenido: str, destinatario: str):
        ...