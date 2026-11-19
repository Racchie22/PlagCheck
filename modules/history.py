
"""SQLite-based comparison history for PlagCheck."""

import json
import sqlite3
from pathlib import Path

DB_PATH = Path("data") / "plagcheck.db"

def init_db(db_path: Path = DB_PATH) -> None:
    """Create the database and history table if they do not exist."""

    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(db_path) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS comparison_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                comparison_type TEXT NOT NULL,
                source_name TEXT NOT NULL,
                target_name TEXT NOT NULL,
                similarity REAL NOT NULL,
                matches TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)


def save_comparison(
    comparison_type: str,
    source_name: str,
    target_name: str,
    similarity: float,
    matches: list,
    db_path: Path = DB_PATH,
) -> int:
    """Save a comparison and return its unique history ID."""

    if comparison_type not in {"Text", "Document"}:
        raise ValueError("Comparison type must be Text or Document.")

    if not isinstance(source_name, str) or not source_name.strip():
        raise ValueError("Source name cannot be empty.")

    if not isinstance(target_name, str) or not target_name.strip():
        raise ValueError("Target name cannot be empty.")

    if not isinstance(similarity, (int, float)) or not 0 <= similarity <= 100:
        raise ValueError("Similarity must be between 0 and 100.")

    if not isinstance(matches, list):
        raise TypeError("Matches must be provided as a list.")

    init_db(db_path)

    with sqlite3.connect(db_path) as connection:
        cursor = connection.execute("""
            INSERT INTO comparison_history (
                comparison_type,
                source_name,
                target_name,
                similarity,
                matches
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            comparison_type,
            source_name.strip(),
            target_name.strip(),
            float(similarity),
            json.dumps(matches),
        ))

        return cursor.lastrowid


def get_history(db_path: Path = DB_PATH) -> list[dict]:
    """Return all saved comparisons, newest first."""

    init_db(db_path)

    with sqlite3.connect(db_path) as connection:
        connection.row_factory = sqlite3.Row

        rows = connection.execute("""
            SELECT * FROM comparison_history
            ORDER BY id DESC
        """).fetchall()

    history = []

    for row in rows:
        record = dict(row)
        record["matches"] = json.loads(record["matches"])
        history.append(record)

    return history


def get_comparison_by_id(
    comparison_id: int,
    db_path: Path = DB_PATH,
) -> dict | None:
    """Retrieve one comparison using its unique ID."""

    init_db(db_path)

    with sqlite3.connect(db_path) as connection:
        connection.row_factory = sqlite3.Row

        row = connection.execute("""
            SELECT * FROM comparison_history
            WHERE id = ?
        """, (comparison_id,)).fetchone()

    if row is None:
        return None

    record = dict(row)
    record["matches"] = json.loads(record["matches"])
    return record
