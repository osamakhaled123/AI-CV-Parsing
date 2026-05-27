import pdfplumber
from pathlib import Path


def extract_pdf(file_path: str) -> str:
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    return text

def extract_text(file_path: str):
    ext = Path(file_path).suffix.lower()
    
    if ext == ".pdf":
        return extract_pdf(file_path)
    
    elif ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
        
    else:
        raise ValueError("Unsupported file type")    