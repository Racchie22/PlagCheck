
import pytest

from modules.dashboard import summarize_history


def test_empty_history():
    result = summarize_history([])

    assert result["total"] == 0
    assert result["average_similarity"] == 0.0
    assert result["highest_similarity"] == 0.0
    assert result["lowest_similarity"] == 0.0
    assert result["text_count"] == 0
    assert result["document_count"] == 0
    assert result["recent"] == []


def test_dashboard_statistics():
    history = [
        {"comparison_type": "Document", "similarity": 80.0},
        {"comparison_type": "Text", "similarity": 60.0},
        {"comparison_type": "Text", "similarity": 40.0},
    ]

    result = summarize_history(history)

    assert result["total"] == 3
    assert result["average_similarity"] == 60.0
    assert result["highest_similarity"] == 80.0
    assert result["lowest_similarity"] == 40.0
    assert result["text_count"] == 2
    assert result["document_count"] == 1


def test_recent_history_is_limited_to_five():
    history = [
        {"comparison_type": "Text", "similarity": float(i)}
        for i in range(10)
    ]

    result = summarize_history(history)

    assert len(result["recent"]) == 5
    assert result["recent"] == history[:5]


def test_invalid_history_type():
    with pytest.raises(TypeError):
        summarize_history("not a list")
