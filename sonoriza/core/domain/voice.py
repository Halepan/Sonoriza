from dataclasses import dataclass
from sonoriza.core.enums.enums import Genero, Calidad

@dataclass(frozen=True)
class Voice:
    genero: Genero
    calidad: Calidad
    velocidad: int

    def __post_init__(self) -> None:
        if self.velocidad <= 0:
            raise ValueError("La velocidad debe ser > 0.")