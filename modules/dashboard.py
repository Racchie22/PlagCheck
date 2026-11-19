
"""Dashboard statistics for PlagCheck."""


def summarize_history(history: list[dict]) -> dict:
    """Calculate dashboard metrics from comparison history."""

    if not isinstance(history, list):
        raise TypeError("History must be a list.")

    if not history:
        return {
            "total": 0,
            "average_similarity": 0.0,
            "highest_similarity": 0.0,
            "lowest_similarity": 0.0,
            "text_count": 0,
            "document_count": 0,
            "recent": [],
        }

    scores = [record["similarity"] for record in history]

    text_count = sum(
        record["comparison_type"] == "Text"
        for record in history
    )

    document_count = sum(
        record["comparison_type"] == "Document"
        for record in history
    )

    return {
        "total": len(history),
        "average_similarity": round(sum(scores) / len(scores), 2),
        "highest_similarity": round(max(scores), 2),
        "lowest_similarity": round(min(scores), 2),
        "text_count": text_count,
        "document_count": document_count,
        "recent": history[:5],
    }
