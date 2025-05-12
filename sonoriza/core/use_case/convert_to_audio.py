from dataclasses import dataclass
from sonoriza.core.domain import Document, AudioConfig, Voice
from sonoriza.core.services import IDocumentReader, ITxt_to_speech

@dataclass
class Convert_audio:
    documento: Document
    reader: IDocumentReader
    traductor : ITxt_to_speech

    def get(self)->bytes:
        text = self.reader.extract_text(self.documento.ruta)
        return self.traductor.convertir_texto(texto= text)
        


