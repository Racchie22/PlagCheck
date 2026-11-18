"""Sentence-level matching helpers for PlagCheck."""

import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from modules.preprocessing import preprocess_text


DEFAULT_MATCH_THRESHOLD = 50.0



def split_sentences(text: str) -> list[str]:
    """Split text into sentences while handling PDF line breaks."""

    if not isinstance(text, str):
        raise TypeError("Input text must be a string.")

    # PDF extraction often inserts newlines between words.
    # Convert all whitespace sequences into normal spaces.
    cleaned_text = re.sub(r"\s+", " ", text.strip())

    # Split only at sentence-ending punctuation.
    parts = re.split(r"(?<=[.!?])\s+", cleaned_text)

    # Ignore short fragments such as headings and isolated words.
    sentences = [
        part.strip()
        for part in parts
        if len(part.strip().split()) >= 2
    ]

    return sentences


def find_matching_sentences(
    text_a: str,
    text_b: str,
    threshold: float = DEFAULT_MATCH_THRESHOLD,
) -> list[dict[str, float | str]]:
    """Find the best sentence match in Text B for each sentence in Text A."""
    if not isinstance(text_a, str) or not isinstance(text_b, str):
        raise TypeError("Both inputs must be strings.")
    if not isinstance(threshold, (int, float)) or not 0 <= threshold <= 100:
        raise ValueError("Threshold must be a number between 0 and 100.")

    sentences_a = split_sentences(text_a)
    sentences_b = split_sentences(text_b)
    if not sentences_a or not sentences_b:
        raise ValueError("Both text samples must contain at least one sentence.")

    valid_a = [(s, preprocess_text(s)) for s in sentences_a]
    valid_b = [(s, preprocess_text(s)) for s in sentences_b]
    valid_a = [(s, cleaned) for s, cleaned in valid_a if cleaned]
    valid_b = [(s, cleaned) for s, cleaned in valid_b if cleaned]
    if not valid_a or not valid_b:
        raise ValueError("Both text samples must contain words that can be compared.")

    original_a, cleaned_a = zip(*valid_a)
    original_b, cleaned_b = zip(*valid_b)
    vectorizer = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
    try:
        vectors = vectorizer.fit_transform(list(cleaned_a) + list(cleaned_b))
    except ValueError as exc:
        raise ValueError("Both text samples must contain words that can be compared.") from exc

    matrix_a = vectors[:len(cleaned_a)]
    matrix_b = vectors[len(cleaned_a):]
    scores = cosine_similarity(matrix_a, matrix_b)

    matches = []
    for index, row in enumerate(scores):
        best_index = int(row.argmax())
        score = float(row[best_index]) * 100
        if score >= threshold:
            matches.append({
                "sentence_a": original_a[index],
                "sentence_b": original_b[best_index],
                "similarity": round(score, 2),
            })
    return matches
