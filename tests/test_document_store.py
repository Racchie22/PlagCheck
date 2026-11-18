
from pathlib import Path

import pytest

from modules.document_store import (
    save_document,
    get_stored_documents,
    compare_with_collection,
)


def test_save_document(tmp_path):
    saved_path = save_document(
        "sample.txt",
        b"This is a sample document.",
        tmp_path,
    )

    assert saved_path.exists()
    assert saved_path.name == "sample.txt"


def test_duplicate_filename(tmp_path):
    first = save_document("sample.txt", b"First document.", tmp_path)
    second = save_document("sample.txt", b"Second document.", tmp_path)

    assert first != second
    assert first.exists()
    assert second.exists()


def test_get_stored_documents(tmp_path):
    save_document("one.txt", b"First document.", tmp_path)
    save_document("two.txt", b"Second document.", tmp_path)

    documents = get_stored_documents(tmp_path)

    assert len(documents) == 2


def test_compare_with_collection(tmp_path):
    save_document(
        "similar.txt",
        b"Machine learning is a useful technology.",
        tmp_path,
    )
    save_document(
        "different.txt",
        b"Apples and oranges are different fruits.",
        tmp_path,
    )

    results = compare_with_collection(
        "Machine learning is a useful technology.",
        tmp_path,
    )

    assert len(results) == 2
    assert results[0]["document_name"] == "similar.txt"
    assert results[0]["similarity"] > results[1]["similarity"]


def test_empty_collection(tmp_path):
    results = compare_with_collection(
        "Some sample text.",
        tmp_path,
    )

    assert results == []


def test_invalid_document_not_saved(tmp_path):
    with pytest.raises(ValueError):
        save_document("image.jpg", b"not a document", tmp_path)

    assert get_stored_documents(tmp_path) == []
