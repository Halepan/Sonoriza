from pathlib import Path
from sonoriza.infrastucture.document_readers import (
    DOCXReader, PDFReader, ODTReader,
    TXTReader, RTFReader, HTMLReader,
    PPTXReader,EPUBReader,XLSXReader
)
from sonoriza.core.services.document_reader import IDocumentReader
from sonoriza.core.enums.enums import DocumentType

def get_reader(ext:str) -> IDocumentReader:
    """Devuelve el lector adecuado según la extensión del archivo"""
    
    readers = {
        DocumentType.DOCX: DOCXReader(),
        DocumentType.PDF: PDFReader(),
        DocumentType.ODT: ODTReader(),
        DocumentType.TXT: TXTReader(),
        DocumentType.RTF: RTFReader(),
        DocumentType.HTML: HTMLReader(),
        DocumentType.EPUB: EPUBReader(),
        DocumentType.PPTX: PPTXReader(),
        DocumentType.XLSX: XLSXReader()
    }
        
    return readers[ext]