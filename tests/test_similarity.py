"""Tests for PlagCheck similarity calculations."""

import pytest

from modules.similarity import calculate_similarity


def test_identical_text_has_100_percent_similarity():
    text = "PlagCheck compares two text samples."
    assert calculate_similarity(text, text) == 100.0


def test_case_and_punctuation_do_not_change_similarity():
    assert calculate_similarity("HELLO, WORLD!", "hello world") == 100.0


def test_unrelated_text_has_zero_similarity():
    score = calculate_similarity(
        "apple banana orange",
        "computer keyboard monitor",
    )
    assert score == 0.0


def test_partial_overlap_is_between_zero_and_one_hundred():
    score = calculate_similarity(
        "the quick brown fox jumps over the fence",
        "the quick brown dog sleeps near the fence",
    )
    assert 0.0 < score < 100.0


@pytest.mark.parametrize("first,second", [("", "some text"), ("some text", "   "), ("", "")])
def test_empty_inputs_are_rejected(first, second):
    with pytest.raises(ValueError):
        calculate_similarity(first, second)


def test_non_string_input_is_rejected():
    with pytest.raises(TypeError):
        calculate_similarity(None, "some text")
