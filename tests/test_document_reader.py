
from io import BytesIO

import pytest
from docx import Document
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    PageBreak,
)
from reportlab.lib.styles import getSampleStyleSheet

from modules.document_reader import extract_text


def test_extract_txt():
    content = b"Hello PlagCheck"
    result = extract_text("sample.txt", content)

    assert result == "Hello PlagCheck"


def test_extract_docx():
    document = Document()
    document.add_paragraph("Hello PlagCheck")

    buffer = BytesIO()
    document.save(buffer)

    result = extract_text("sample.docx", buffer.getvalue())

    assert "Hello PlagCheck" in result


def test_unsupported_file():
    with pytest.raises(ValueError):
        extract_text("sample.jpg", b"image data")


def test_empty_txt():
    with pytest.raises(ValueError):
        extract_text("empty.txt", b"   ")


def test_invalid_file_content():
    with pytest.raises(ValueError):
        extract_text("sample.pdf", b"not a valid PDF")


def test_extract_pdf_multiple_pages():
    buffer = BytesIO()
    styles = getSampleStyleSheet()

    document = SimpleDocTemplate(buffer)

    content = [
        Paragraph("First page unique marker.", styles["BodyText"]),
        PageBreak(),
        Paragraph("Second page unique marker.", styles["BodyText"]),
    ]

    document.build(content)

    extracted_text = extract_text(
        "multipage.pdf",
        buffer.getvalue(),
    )

    assert "First page unique marker." in extracted_text
    assert "Second page unique marker." in extracted_text
