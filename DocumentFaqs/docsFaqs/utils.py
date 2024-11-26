from pathlib import Path
from PyPDF2 import PdfReader
from main import settings


def extract_text_from_pdf(file_path):
    """
    Extract text content from a PDF file.
    """
    fpath = str(file_path)
    fpath = fpath.split('/')
    file_path = str(settings.BASE_DIR) + "\\media\\" + fpath[-1]
    
    reader = PdfReader(file_path)
    content = ""
    for page in reader.pages:
        content += page.extract_text()
    return content