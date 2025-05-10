from pathlib import Path
from pptx import Presentation
from core.services.document_reader import IDocumentReader

class PPTXReader(IDocumentReader):
    @property
    def supported_formats(self) -> list[str]:
        return ['pptx']

    def extract_text(self, file_path: Path) -> str:
        """Extrae texto de presentaciones PPTX usando python-pptx"""
        prs = Presentation(file_path)
        full_text = []
        
        for slide in prs.slides:
            for shape in slide.shapes:
                if hasattr(shape, "text"):
                    full_text.append(shape.text)
        
        return '\n'.join(full_text)