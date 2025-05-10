from pathlib import Path
from core.services.document_reader import IDocumentReader

class TXTReader(IDocumentReader):
    @property
    def supported_formats(self) -> list[str]:
        return ['txt']

    def extract_text(self, file_path: Path) -> str:
        """Lee archivos de texto plano"""
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()