from sonoriza.core.domain.document import Document

def text():
    ruta = input("ruta: ")

    archivo = Document(ruta)
    print(archivo)