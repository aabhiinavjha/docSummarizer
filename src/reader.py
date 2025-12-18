import os
from PyPDF2 import PdfReader
from docx import Document


def read_txt(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def read_pdf(path):
    reader = PdfReader(path)
    return " ".join(page.extract_text() or "" for page in reader.pages)


def read_docx(path):
    doc = Document(path)
    return " ".join(p.text for p in doc.paragraphs)


def read_document(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".txt":
        return read_txt(path)
    elif ext == ".pdf":
        return read_pdf(path)
    elif ext == ".docx":
        return read_docx(path)
    else:
        raise ValueError("Unsupported file format: %s" % ext)
