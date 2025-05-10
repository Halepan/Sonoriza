from pathlib import Path
from sonoriza.infrastucture.document_readers import (
    DOCXReader, PDFReader, ODTReader,
    TXTReader, RTFReader, HTMLReader,
    PPTXReader,EPUBReader,XLSXReader
)
from core.services.document_reader import IDocumentReader

def get_reader(ext:str) -> IDocumentReader:
    """Devuelve el lector adecuado según la extensión del archivo"""
    
    readers = {
        'docx': DOCXReader(),
        'pdf': PDFReader(),
        'odt': ODTReader(),
        'txt': TXTReader(),
        'rtf': RTFReader(),
        'html': HTMLReader(),
        'htm': HTMLReader(),
        'epub': EPUBReader(),
        'pptx': PPTXReader(),
        'xlsx': XLSXReader(),
    }
    
    if ext not in readers:
        raise ValueError(f"Formato no soportado: {ext}")
    
    return readers[ext]