from pathlib import Path
from sonoriza.core.enums.enums import DocumentType
from typing import Optional

class Document:
    def __init__(self, ruta: str, nombre: Optional[str] = None) -> None:
        self._ruta = Path(ruta)
        self._nombre = nombre or self._ruta.stem  # Usa el nombre del archivo si no se provee
        self._tipo = self._infer_type()
        self._validate()

    def _infer_type(self) -> DocumentType:
        """Infiere el tipo de documento desde la extensión del archivo."""
        ext = self._ruta.suffix[1:]  # Elimina el punto (ej: '.pdf' -> 'pdf')
        try:
            return DocumentType.from_extension(ext)
        except ValueError as e:
            raise ValueError(f"Formato no soportado para el archivo '{self._ruta}': {str(e)}")

    def _validate(self) -> None:
        if not self._ruta.exists():
            raise FileNotFoundError(f"El archivo '{self._ruta}' no existe.")

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def ruta(self) -> Path:
        return self._ruta

    @property
    def tipo(self) -> DocumentType:
        return self._tipo

    @property
    def reader_class_name(self) -> str:
        return self._tipo.reader_class_name