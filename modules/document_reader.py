
"""Document text extraction helpers for PlagCheck."""

from io import BytesIO
from pathlib import Path

from docx import Document
from pypdf import PdfReader


SUPPORTED_EXTENSIONS = {".txt", ".pdf", ".docx"}


def extract_text(file_name: str, file_content: bytes) -> str:
    """Extract text from a supported document using its filename and bytes."""

    if not isinstance(file_name, str) or not isinstance(file_content, bytes):
        raise TypeError("Filename must be a string and file content must be bytes.")

    extension = Path(file_name).suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError("Unsupported file type. Upload TXT, PDF or DOCX.")

    try:
        if extension == ".txt":
            text = file_content.decode("utf-8-sig")

        elif extension == ".pdf":
            reader = PdfReader(BytesIO(file_content))
            text = "\n".join(
                page.extract_text() or "" for page in reader.pages
            )

        else:  # DOCX
            document = Document(BytesIO(file_content))
            text = "\n".join(
                paragraph.text for paragraph in document.paragraphs
            )

    except Exception as error:
        raise ValueError(
            f"Could not read {file_name}. The file may be damaged or unreadable."
        ) from error

    if not text.strip():
        raise ValueError(
            f"No readable text was found in {file_name}."
        )

    return text
