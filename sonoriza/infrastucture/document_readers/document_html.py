from pathlib import Path
from bs4 import BeautifulSoup
from sonoriza.core.services.document_reader import IDocumentReader
from sonoriza.core.enums import DocumentType

class HTMLReader(IDocumentReader):
    @property
    def supported_formats(self) -> list[str]:
        return [DocumentType.HTML]

    def extract_text(self, file_path: Path) -> str:
        """Extrae texto de HTML usando BeautifulSoup"""
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file.read(), 'html.parser')
            return soup.get_text(separator='\n', strip=True)