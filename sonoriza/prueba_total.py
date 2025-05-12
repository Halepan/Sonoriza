from sonoriza.core.domain import AudioConfig, Voice, Document
from sonoriza.core.enums.enums import Genero, Calidad, AudioFormat
from sonoriza.core.use_case.convert_to_audio import Convert_audio
from sonoriza.infrastucture.document_readers.reader_factory import get_reader
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

audio = Pyttsx3Adapter(config)
arch = Document(ruta= ruta)
audio_wav = Convert_audio(arch,get_reader(arch.tipo),audio)

# Guardar el WAV
with open(config.output_dir / f"{arch.nombre}.wav", "wb") as f:
    f.write(audio_wav.get())