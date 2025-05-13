from dataclasses import dataclass
from sonoriza.core.domain import Document, AudioConfig
from sonoriza.core.services import IDocumentReader, ITxt_to_speech

@dataclass
class Convert_audio:
    """
    Caso de uso para convertir documentos a audio.
    Responsabilidades:
    - Coordinar el flujo: leer documento → convertir texto → retornar audio
    - Validar precondiciones
    """
    reader: IDocumentReader
    tts_service: ITxt_to_speech
    output_config: AudioConfig

    def execute(self, document: Document) -> bytes:
        """
        Ejecuta la conversión con manejo de errores específicos del dominio
        """
        self._validate_document(document)
        
        try:
            text = self.reader.extract_text(document.ruta)
            return self.tts_service.convertir_texto(text)
        except Exception as e:
            raise AudioConversionError(
                f"Error procesando {document.nombre}: {str(e)}"
            ) from e

    def _validate_document(self, document: Document) -> None:
        """Validaciones de dominio centralizadas"""
        if not document.ruta.exists():
            raise FileNotFoundError(f"Documento no encontrado: {document.ruta}")
        print(document.tipo)
        print(self.reader.supported_formats)
        if document.tipo not in self.reader.supported_formats:
            raise UnsupportedFormatError(
                f"Formato {document.tipo.name} no soportado por este lector"
            )


# Errores específicos del dominio
class AudioConversionError(Exception):
    """Error durante la conversión de audio"""
    pass

class UnsupportedFormatError(Exception):
    """Formato de documento no soportado"""
    pass