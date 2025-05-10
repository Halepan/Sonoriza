from pathlib import Path
import docx
from core.services.document_reader import IDocumentReader

class DOCXReader(IDocumentReader):
    @property
    def supported_formats(self) -> list[str]:
        return ['docx']

    def extract_text(self, file_path: Path) -> str:
        """Extrae texto de archivos .docx usando python-docx"""
        doc = docx.Document(file_path)
        full_text = []
        for paragraph in doc.paragraphs:
            full_text.append(paragraph.text)
        return '\n'.join(full_text)