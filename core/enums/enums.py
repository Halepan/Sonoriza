from enum import Enum, auto

class Genero(Enum):
    HOMBRE = auto()
    MUJER = auto()

    @classmethod
    def default(cls) -> "Genero":
        return cls.HOMBRE

class Calidad(Enum):
    BUENA = auto()
    ALTA = auto()
    PREMIUM = auto()  # Ejemplo de extensión

    @classmethod
    def from_str(cls, value: str) -> "Calidad":
        return cls[value.upper()]

class DocumentType(Enum):
    """Tipos de documentos soportados, con metadatos para su manejo."""
    
    # Valores principales
    DOCX = auto()
    ODT = auto()
    TXT = auto()
    RTF = auto()
    HTML = auto()
    PDF = auto()
    EPUB = auto()
    
    # Opcionales (excel/powerpoint)
    XLSX = auto()
    PPTX = auto()

    # ---- Métodos de utilidad ----
    @classmethod
    def from_extension(cls, ext: str) -> "DocumentType":
        """Obtiene el tipo desde una extensión (sin punto). Ej: 'pdf' -> DocumentType.PDF"""
        ext_map = {
            'docx': cls.DOCX,
            'odt': cls.ODT,
            'txt': cls.TXT,
            'rtf': cls.RTF,
            'html': cls.HTML,
            'pdf': cls.PDF,
            'epub': cls.EPUB,
            'xlsx': cls.XLSX,
            'pptx': cls.PPTX
        }
        try:
            return ext_map[ext.lower()]
        except KeyError:
            raise ValueError(f"Extensión '{ext}' no soportada")

    @property
    def reader_class_name(self) -> str:
        """Nombre de la clase lectora asociada en infrastructure. Ej: PDF -> 'PDFReader'"""
        return f"{self.name}Reader"