sonoriza/
├── core/
│   ├── persistence/           # Nuevo módulo
│   │   ├── progress_tracker.py
│   │   └── task_recovery.py   # Lógica para recuperar tareas
│   ├── domain/                 # Modelos de datos
│   │   ├── document.py         # Clase Documento
│   │   └── voice.py            # Configuración de voz
│   │   |__ audi.py             # Configuracion del audio
|   |     
│   ├── services/               # Interfaces de servicios
│   │   ├── text_to_speech.py   # ITTS
│   │   └── document_reader.py  # IDocumentReader
│   │
│   └── use_cases/              # Casos de uso
│       ├── convert_to_audio.py
│       └── split_audio.py
│
├── infrastructure/             # Implementaciones concretas
│   ├── audio/
│   │   ├── pyttsx3_adapter.py  # TTS offline
│   │   └── audio_exporter.py   # Exportar a MP3/WAV
│   │
│   ├── document_readers/       # Lectores de documentos
│   │   ├── docx_reader.py      # .docx (python-docx)
│   │   ├── odt_reader.py       # .odt (odfpy)
│   │   └── txt_reader.py       # .txt (built-in)
│   │
│   └── voice_management/
│       └── windows_voice.py    # Gestión de voces Windows
│
├── ui/                        # interfaz grafica
│   ├── workers/               # Hilos para segundo plano
│   │   └── conversion_worker.py
│   ├── main_window.py          # Ventana principal (PyQt5)
│   ├── components/             # Widgets reutilizables
│   │   ├── file_selector.py
│   │   └── progress_bar.py
│   └── resources/             # Assets (opcional)
│       ├── icons/
│       └── styles.qss
│
├── app.py                      # Punto de entrada
├── requirements.txt            # Dependencias
├── .gitignore                  # Archivos ignorados
└── README.md                   # Documentación