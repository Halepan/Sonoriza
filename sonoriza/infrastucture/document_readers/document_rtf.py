from pathlib import Path
import striprtf
from core.services.document_reader import IDocumentReader

class RTFReader(IDocumentReader):
    @property
    def supported_formats(self) -> list[str]:
        return ['rtf']

    def extract_text(self, file_path: Path) -> str:
        """Procesa .rtf usando striprtf"""
        with open(file_path, 'r', encoding='utf-8') as file:
            rtf_text = file.read()
            return striprtf.rtf_to_text(rtf_text)