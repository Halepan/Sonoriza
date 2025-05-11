from sonoriza.core.use_case.convert_to_audio import convert_audi
from sonoriza.core.domain.document import Document
from sonoriza.infrastucture.document_readers.reader_factory import get_reader


rout = input("ruta: ")
archiv = Document(ruta= rout)
print(convert_audi(archiv,get_reader(archiv.tipo)))
