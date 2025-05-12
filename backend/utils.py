import fitz
import os

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = "\n".join(page.get_text() for page in doc)
    return text

def save_project(name, text):
    path = f"data/projects/{name}.txt"
    with open(path, "w") as f:
        f.write(text)
