"""Tests for PlagCheck text preprocessing."""

import pytest

from modules.preprocessing import preprocess_text


def test_preprocess_lowercases_text():
    assert preprocess_text("HELLO World") == "hello world"


def test_preprocess_replaces_punctuation_and_collapses_spaces():
    assert preprocess_text("Hello,   world!\nAgain.") == "hello world again"


def test_preprocess_keeps_original_words_and_numbers():
    assert preprocess_text("Python 3 is Great") == "python 3 is great"


def test_preprocess_rejects_non_string_input():
    with pytest.raises(TypeError):
        preprocess_text(None)
