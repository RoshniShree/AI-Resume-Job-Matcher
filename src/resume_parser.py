from pypdf import PdfReader


def extract_text_from_pdf(file_object) -> str:
    """Extract selectable text from a PDF file-like object."""
    reader = PdfReader(file_object)
    return "\n".join(page.extract_text() or "" for page in reader.pages).strip()
