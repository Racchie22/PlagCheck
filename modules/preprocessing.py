"""Text normalisation helpers used by the PlagCheck comparison engine."""

import re
import string


def preprocess_text(text: str) -> str:
    """Normalise text for comparison without modifying the original input.

    The function lowercases text, replaces punctuation with spaces, collapses
    repeated whitespace, and returns a stripped string.
    """
    if not isinstance(text, str):
        raise TypeError("Input text must be a string.")

    text = text.lower()
    punctuation_table = str.maketrans({character: " " for character in string.punctuation})
    text = text.translate(punctuation_table)
    text = re.sub(r"\s+", " ", text)
    return text.strip()
