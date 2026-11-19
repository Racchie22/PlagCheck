
import pytest

from modules.history import (
    init_db,
    save_comparison,
    get_history,
    get_comparison_by_id,
)


def test_database_is_created(tmp_path):
    db_path = tmp_path / "test.db"

    init_db(db_path)

    assert db_path.exists()


def test_save_comparison(tmp_path):
    db_path = tmp_path / "test.db"

    comparison_id = save_comparison(
        "Text",
        "Text 1",
        "Text 2",
        75.5,
        [],
        db_path,
    )

    assert comparison_id == 1


def test_get_history(tmp_path):
    db_path = tmp_path / "test.db"

    save_comparison("Text", "A", "B", 75.5, [], db_path)
    save_comparison("Document", "A.pdf", "B.pdf", 60.0, [], db_path)

    history = get_history(db_path)

    assert len(history) == 2
    assert history[0]["comparison_type"] == "Document"


def test_matches_are_stored_and_retrieved(tmp_path):
    db_path = tmp_path / "test.db"

    matches = [
        {
            "sentence_a": "Hello world.",
            "sentence_b": "Hello world!",
            "similarity": 100.0,
        }
    ]

    comparison_id = save_comparison(
        "Text", "A", "B", 100, matches, db_path
    )

    record = get_comparison_by_id(comparison_id, db_path)

    assert record["matches"] == matches


def test_get_nonexistent_comparison(tmp_path):
    record = get_comparison_by_id(999, tmp_path / "test.db")

    assert record is None


def test_invalid_comparison_type(tmp_path):
    with pytest.raises(ValueError):
        save_comparison(
            "Image", "A", "B", 50, [], tmp_path / "test.db"
        )


def test_invalid_similarity(tmp_path):
    with pytest.raises(ValueError):
        save_comparison(
            "Text", "A", "B", 150, [], tmp_path / "test.db"
        )
