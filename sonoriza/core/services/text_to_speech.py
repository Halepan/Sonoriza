from abc import ABC, abstractmethod
from sonoriza.core.domain.audi import AudioConfig

class ITxt_to_speech(ABC):
    def __init__(self, config: AudioConfig):  # Solo AudioConfig
        self.config = config
    
    @abstractmethod
    def convertir_texto(self, texto: str) -> bytes:
        """Usa self.config.voice y self.config.format internamente"""
        pass