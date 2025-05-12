# infrastructure/audio/pyttsx3_adapter.py
import pyttsx3
import tempfile
import os
from sonoriza.core.services.text_to_speech import ITxt_to_speech
from sonoriza.core.domain.audi import AudioConfig

class Pyttsx3Adapter(ITxt_to_speech):
    def __init__(self, config: AudioConfig):
        # Fuerza el formato WAV aunque el config diga otra cosa
        if config.format.name != "WAV":
            print("[Advertencia] Sobreescribiendo formato a WAV (soporte nativo)")
        self.config = config
        self.engine = self._configure_engine()

    def _configure_engine(self):
        engine = pyttsx3.init()
        
        # Configuración básica de voz
        voices = engine.getProperty('voices')
        for voice in voices:
            if "spanish" in voice.name.lower() or "español" in voice.name.lower():
                if self.config.voice.genero.name == "HOMBRE" and "male" in voice.name.lower():
                    engine.setProperty('voice', voice.id)
                    break
                elif self.config.voice.genero.name == "MUJER" and "female" in voice.name.lower():
                    engine.setProperty('voice', voice.id)
                    break
        
        # Ajustes de calidad/velocidad
        engine.setProperty('rate', 130 + (self.config.voice.velocidad * 10))
        engine.setProperty('volume', 0.9 if self.config.voice.calidad.name != "BUENA" else 0.6)
        
        return engine

    def convertir_texto(self, texto: str) -> bytes:
        """Devuelve audio en formato WAV como bytes"""
        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp_file:
            temp_path = tmp_file.name
        
        try:
            self.engine.save_to_file(texto, temp_path)
            self.engine.runAndWait()
            
            with open(temp_path, 'rb') as f:
                return f.read()
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)