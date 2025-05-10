from pathlib import Path
from ebooklib import epub
from bs4 import BeautifulSoup
from core.services.document_reader import IDocumentReader

class EPUBReader(IDocumentReader):
    @property
    def supported_formats(self) -> list[str]:
        return ['epub']

    def extract_text(self, file_path: Path) -> str:
        """Extrae texto de archivos EPUB usando ebooklib"""
        book = epub.read_epub(file_path)
        full_text = []
        
        for item in book.get_items():
            if item.get_type() == epub.ITEM_DOCUMENT:
                soup = BeautifulSoup(item.get_content(), 'html.parser')
                full_text.append(soup.get_text(separator='\n'))
        
        return '\n\n'.join(full_text)