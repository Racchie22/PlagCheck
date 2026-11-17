"""TF-IDF and cosine-similarity functions for PlagCheck."""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from modules.preprocessing import preprocess_text


def calculate_similarity(text_a: str, text_b: str) -> float:
    """Return cosine similarity as a percentage between 0 and 100.

    Both inputs are preprocessed before vectorisation. Empty inputs and inputs
    that contain no usable terms after preprocessing are rejected.
    """
    if not isinstance(text_a, str) or not isinstance(text_b, str):
        raise TypeError("Both inputs must be strings.")

    cleaned_a = preprocess_text(text_a)
    cleaned_b = preprocess_text(text_b)

    if not cleaned_a or not cleaned_b:
        raise ValueError("Both text samples must contain non-empty text.")

    vectorizer = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
    try:
        vectors = vectorizer.fit_transform([cleaned_a, cleaned_b])
    except ValueError as exc:
        raise ValueError("Both text samples must contain words that can be compared.") from exc

    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(float(score) * 100, 2)
