import pdfplumber
from pathlib import Path
from models import ProcessingEnum, ResponseSignal
from fastapi.responses import JSONResponse
from fastapi import status

def extract_pdf(file_path: str) -> str:
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    return text

def extract_text(file_path: str):
    ext = Path(file_path).suffix.lower()
    
    if ext == ProcessingEnum.PDF.value:
        return extract_pdf(file_path)
    
    elif ext == ProcessingEnum.TXT.value:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
        
    else:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "signal":ResponseSignal.NO_CVS_FOUND.value,
                "ext":ext
            }
        )