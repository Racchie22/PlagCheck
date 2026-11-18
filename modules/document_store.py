
"""Local document collection and comparison helpers."""

from pathlib import Path
import re

from modules.document_reader import extract_text
from modules.similarity import calculate_similarity


DOCUMENTS_DIR = Path("data") / "documents"


def _safe_filename(filename: str) -> str:
    """Remove directory components and unsafe filename characters."""
    name = Path(filename).name
    name = re.sub(r"[^A-Za-z0-9._ -]", "_", name)
    if not name or name in {".", ".."}:
        raise ValueError("Invalid document filename.")
    return name


def save_document(
    filename: str,
    file_content: bytes,
    storage_dir: Path = DOCUMENTS_DIR,
) -> Path:
    """Save a supported document in the local collection."""

    safe_name = _safe_filename(filename)

    # Validate and extract text before saving.
    extract_text(safe_name, file_content)

    storage_dir.mkdir(parents=True, exist_ok=True)

    destination = storage_dir / safe_name

    # Avoid overwriting an existing document.
    if destination.exists():
        stem = destination.stem
        suffix = destination.suffix
        counter = 1

        while destination.exists():
            destination = storage_dir / f"{stem}_{counter}{suffix}"
            counter += 1

    destination.write_bytes(file_content)
    return destination


def get_stored_documents(
    storage_dir: Path = DOCUMENTS_DIR,
) -> list[Path]:
    """Return supported documents from the local collection."""

    if not storage_dir.exists():
        return []

    supported = {".txt", ".pdf", ".docx"}

    return sorted(
        path for path in storage_dir.iterdir()
        if path.is_file() and path.suffix.lower() in supported
    )


def compare_with_collection(
    uploaded_text: str,
    storage_dir: Path = DOCUMENTS_DIR,
) -> list[dict[str, str | float]]:
    """Compare uploaded text against every readable stored document."""

    results = []

    for document_path in get_stored_documents(storage_dir):
        try:
            stored_content = document_path.read_bytes()
            stored_text = extract_text(
                document_path.name,
                stored_content,
            )

            score = calculate_similarity(uploaded_text, stored_text)

            results.append({
                "document_name": document_path.name,
                "similarity": score,
            })

        except (ValueError, TypeError):
            # Skip unreadable documents rather than stopping all comparisons.
            continue

    return sorted(
        results,
        key=lambda result: result["similarity"],
        reverse=True,
    )
