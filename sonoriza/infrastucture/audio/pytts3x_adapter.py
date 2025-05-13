# infrastructure/audio/pyttsx3_adapter.py
import pyttsx3
import tempfile
import os
from sonoriza.core.services.text_to_speech import ITxt_to_speech
from sonoriza.core.domain.audi import AudioConfig
from sonoriza.core.enums import Calidad, Genero

class Pyttsx3Adapter(ITxt_to_speech):
    def __init__(self, config: AudioConfig):
        super().__init__(config)
        self.engine = self._configure_engine()

    def _configure_engine(self):
        engine = pyttsx3.init()
        
        # Configuración de voz
        voices = engine.getProperty('voices')
        target_gender = 'male' if self.config.voice.genero == Genero.HOMBRE else 'female'
        
        for voice in voices:
            if target_gender in voice.name.lower():
                if 'spanish' in voice.name.lower() or 'español' in voice.name.lower():
                    engine.setProperty('voice', voice.id)
                    break
        
        # Ajustes de parámetros
        engine.setProperty('rate', 130 + (self.config.voice.velocidad * 15))
        engine.setProperty('volume', {
            Calidad.BUENA: 0.7,
            Calidad.ALTA: 0.85,
            Calidad.PREMIUM: 1.0
        }[self.config.voice.calidad])
        
        return engine

    def convertir_texto(self, texto: str) -> bytes:
        """Devuelve audio en formato WAV crudo (sin exportar)"""
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