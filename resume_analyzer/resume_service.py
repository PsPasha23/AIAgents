from pypdf import PdfReader
from docx import Document

def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from a PDF file.

    """
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text().strip() + "\n"
    return text

def extract_text_from_docx(uploaded_file):
    """
    Extracts text from a DOCX file.

    """
    doc = Document(uploaded_file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text.strip() + "\n"
    return text

def extract_text_from_txt(uploaded_file):
    """
    Extracts text from a TXT file.

    """
    text = uploaded_file.read().decode("utf-8", errors="ignore").strip()
    return text

def extract_resume_text(uploaded_file):
    """
    Determines the file type and extracts text accordingly.

    """
    file_extension = uploaded_file.name.split(".")[-1].lower()
    
    if file_extension == "pdf":
        return extract_text_from_pdf(uploaded_file)
    elif file_extension == "docx":
        return extract_text_from_docx(uploaded_file)
    elif file_extension == "txt":
        return extract_text_from_txt(uploaded_file)
    else:
        raise ValueError("Unsupported file format. Please upload a PDF, DOCX, or TXT file.")