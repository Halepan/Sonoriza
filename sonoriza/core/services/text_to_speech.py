from abc import ABC, abstractmethod
from pathlib import Path
from sonoriza.core.enums.enums import Genero, Calidad

class Txt_to_speech(ABC):
    @abstractmethod
    def traduction(text:str,sexo:Genero,calidad:Calidad)->bytes:
        pass


