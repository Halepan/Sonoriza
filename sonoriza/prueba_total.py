#!/usr/bin/env python3
"""
CLI Tester para el módulo de conversión a audio

Uso profesional:
1. Permite probar con archivos reales
2. Maneja errores específicos del dominio
3. Genera outputs estructurados
"""

import sys
from pathlib import Path
from sonoriza.core.domain import AudioConfig, Voice, Document
from sonoriza.core.enums.enums import Genero, Calidad, AudioFormat
from sonoriza.core.use_case import Convert_audio
from sonoriza.infrastucture.document_readers.reader_factory import get_reader
from sonoriza.infrastucture.audio.pytts3x_adapter import Pyttsx3Adapter
from sonoriza.infrastucture.audio.audio_exporter import AudioExporter

def main():
    try:
        # Configuración interactiva
        ruta_doc = Path(input("\n>>> Ruta absoluta del documento a convertir: ").strip())
        output_dir = Path(input(">>> Directorio de salida (dejar vacío para ./audios): ").strip() or "audios")

        # Configuración de audio
        config = AudioConfig(
            format=AudioFormat.MP3,
            voice=Voice(
                genero=Genero.MUJER,
                calidad=Calidad.ALTA,
                velocidad=5
            ),
            output_dir=output_dir
        )

        # Inicialización de componentes
        documento = Document(ruta=ruta_doc)
        reader = get_reader(documento.tipo)
        tts_service = Pyttsx3Adapter(config)
        
        # Ejecución del caso de uso
        use_case = Convert_audio(
            reader=reader,
            tts_service=tts_service,
            output_config=config
        )
        
        print(f"\n[+] Procesando: {documento.nombre}...")
        audio_data = use_case.execute(documento)
        
        # Exportación
        output_path = config.output_dir / f"{documento.nombre}.{config.format.name.lower()}"
        AudioExporter.save_to_file(audio_data, output_path)
        
        print(f"[✓] Audio generado en: {output_path.resolve()}")

    except FileNotFoundError as e:
        print(f"\n[!] Error: Archivo no encontrado - {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n[!] Error inesperado: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    print("\n" + "═"*50)
    print("  SONORIZA - PRUEBA DE CONVERSIÓN A AUDIO")
    print("═"*50)
    
    main()