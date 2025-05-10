from .document_docx import DOCXReader
from .document_pdf import PDFReader
from .documernt_odt import ODTReader
from .document_txt import TXTReader
from .document_rtf import RTFReader
from .document_html import HTMLReader
from .document_epub import EPUBReader
from .document_pptx import PPTXReader
from .document_xlsx import XLSXReader


__all__ = [
    'DOCXReader', 
    'PDFReader', 
    'ODTReader', 
    'TXTReader', 
    'RTFReader', 
    'HTMLReader',
    'EPUBReader',
    'PPTXReader',
    'XLSXReader'
]