from abc import ABC, abstractmethod
from pathlib import Path

class IDocumentReader(ABC):
    @property
    @abstractmethod
    def supported_formats(self) -> list[str]:
        """Formatos soportados por este lector (ej: ['pdf', 'docx',...])"""
        pass

    @abstractmethod
    def extract_text(self, file_path: Path) -> str:
        """Extrae el texto del documento"""
        pass