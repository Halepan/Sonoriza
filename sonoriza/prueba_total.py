from sonoriza.core.domain import AudioConfig, Voice
from sonoriza.core.enums.enums import Genero, Calidad, AudioFormat
from sonoriza.infrastucture.audio.pytts3x_adapter import Pyttsx3Adapter
from pathlib import Path


ruta = input("ruta: ")
# Configuración (ignorará el formato y siempre usará WAV)
config = AudioConfig(
    format=AudioFormat.WAV,  # ¡Importante! Solo WAV funciona
    voice=Voice(
        genero=Genero.MUJER,
        calidad=Calidad.ALTA,
        velocidad=5  # Rango 1-10
    )
)

adapter = Pyttsx3Adapter(config)
audio_wav = adapter.convertir_texto("Texto de ejemplo para convertir a voz")

# Guardar el WAV
with open(config.output_dir / "salida.wav", "wb") as f:
    f.write(audio_wav)