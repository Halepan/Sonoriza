from pathlib import Path
from odf import text, teletype
from odf.opendocument import load
from core.services.document_reader import IDocumentReader

class ODTReader(IDocumentReader):
    @property
    def supported_formats(self) -> list[str]:
        return ['odt']

    def extract_text(self, file_path: Path) -> str:
        """Extrae texto de .odt usando odfpy"""
        doc = load(file_path)
        full_text = []
        for para in doc.getElementsByType(text.P):
            full_text.append(teletype.extractText(para))
        return '\n'.join(full_text)