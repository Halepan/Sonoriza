from sonoriza.core.domain.document import Document
from sonoriza.core.services.document_reader import IDocumentReader

def convert_audi(document:Document, reader:IDocumentReader)->str:
    text  = reader.extract_text(document.ruta)
    return text
