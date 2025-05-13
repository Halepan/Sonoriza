# infrastructure/audio/audio_exporter.py (versión sin pydub)
import io
from pathlib import Path
from sonoriza.core.enums.enums import AudioFormat

class AudioExporter:
    @staticmethod
    def export_audio(audio_wav: bytes, config) -> bytes:
        """Versión minimalista que solo soporta WAV"""
        if config.format != AudioFormat.WAV:
            raise ValueError("Esta versión solo soporta WAV. Instala FFmpeg para otros formatos.")
        return audio_wav

    @staticmethod
    def save_to_file(audio_data: bytes, output_path: Path):
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(audio_data)