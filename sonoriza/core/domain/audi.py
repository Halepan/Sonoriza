# core/domain/audio.py
from dataclasses import dataclass
from pathlib import Path
from .voice import Voice
from sonoriza.core.enums.enums import AudioFormat

@dataclass(frozen=True)
class AudioConfig:
    format: AudioFormat
    voice: Voice 
    output_dir: Path = Path("audios")
    filename: str = "output"

    def __post_init__(self):
        if not self.output_dir.exists():
            self.output_dir.mkdir(parents=True)