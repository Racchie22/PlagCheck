
import pytest

from io import BytesIO
from pypdf import PdfReader

from modules.report_generator import generate_pdf_report


def test_generate_pdf_report():

    pdf_bytes = generate_pdf_report(
        comparison_type="Text",
        source_name="Text Sample 1",
        target_name="Text Sample 2",
        similarity=75.5,
        matches=[],
    )

    assert isinstance(pdf_bytes, bytes)
    assert pdf_bytes.startswith(b"%PDF")


def test_pdf_contains_comparison_details():

    pdf_bytes = generate_pdf_report(
        "Text",
        "Document A",
        "Document B",
        80.5,
        [],
    )

    reader = PdfReader(BytesIO(pdf_bytes))
    text = "\n".join(page.extract_text() or "" for page in reader.pages)

    assert "Document A" in text
    assert "Document B" in text
    assert "80.50%" in text


def test_pdf_contains_matching_sentences():

    matches = [
        {
            "sentence_a": "Machine learning is useful.",
            "sentence_b": "Machine learning is very useful.",
            "similarity": 85.5,
        }
    ]

    pdf_bytes = generate_pdf_report(
        "Text",
        "A",
        "B",
        85.5,
        matches,
    )

    reader = PdfReader(BytesIO(pdf_bytes))
    text = "\n".join(page.extract_text() or "" for page in reader.pages)

    assert "Machine learning is useful." in text
    assert "Machine learning is very useful." in text


def test_pdf_contains_limitation_note():

    pdf_bytes = generate_pdf_report(
        "Text",
        "A",
        "B",
        50,
        [],
    )

    reader = PdfReader(BytesIO(pdf_bytes))
    text = "\n".join(page.extract_text() or "" for page in reader.pages)

    assert "does not prove" in text


def test_invalid_comparison_type():

    with pytest.raises(ValueError):
        generate_pdf_report(
            "Image",
            "A",
            "B",
            50,
            [],
        )


def test_invalid_similarity():

    with pytest.raises(ValueError):
        generate_pdf_report(
            "Text",
            "A",
            "B",
            150,
            [],
        )


def test_invalid_matches():

    with pytest.raises(TypeError):
        generate_pdf_report(
            "Text",
            "A",
            "B",
            50,
            "not a list",
        )
