
from docx import Document
from io import BytesIO

import pytest

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
