from pathlib import Path
import pdfplumber
from sonoriza.core.services.document_reader import IDocumentReader
from sonoriza.core.enums import DocumentType
class PDFReader(IDocumentReader):
    @property
    def supported_formats(self) -> list[str]:
        return [DocumentType.PDF]

    def extract_text(self, file_path: Path) -> str:
        """Extrae texto de PDFs usando pdfplumber"""
        full_text = []
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                full_text.append(page.extract_text())
        return '\n'.join(full_text)