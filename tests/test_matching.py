"""Tests for sentence-level matching."""

import pytest

from modules.matching import find_matching_sentences, split_sentences


def test_split_sentences_handles_common_punctuation():
    assert split_sentences("First sentence. Second sentence! Third sentence?") == [
        "First sentence.", "Second sentence!", "Third sentence?"
    ]


def test_identical_sentence_is_reported_as_a_full_match():
    sentence = "The earth revolves around the sun."
    matches = find_matching_sentences(sentence, sentence)
    assert len(matches) == 1
    assert matches[0]["sentence_a"] == sentence
    assert matches[0]["sentence_b"] == sentence
    assert matches[0]["similarity"] == 100.0


def test_matching_sentence_is_found_among_other_sentences():
    text_a = "The earth revolves around the sun. Cats are mammals."
    text_b = "The earth revolves around the sun. Water freezes at zero degrees."
    matches = find_matching_sentences(text_a, text_b)
    assert any(match["sentence_a"] == "The earth revolves around the sun." for match in matches)


def test_unrelated_sentences_do_not_pass_default_threshold():
    matches = find_matching_sentences(
        "Apples grow on trees.",
        "A keyboard connects to a computer.",
    )
    assert matches == []


def test_custom_threshold_can_be_used():
    matches = find_matching_sentences(
        "The quick brown fox jumps over the fence.",
        "The quick brown dog sleeps near the fence.",
        threshold=0,
    )
    assert len(matches) == 1
    assert 0 <= matches[0]["similarity"] <= 100


@pytest.mark.parametrize("first,second", [("", "Some sentence."), ("Some sentence.", "  ")])
def test_empty_inputs_are_rejected(first, second):
    with pytest.raises(ValueError):
        find_matching_sentences(first, second)


def test_invalid_threshold_is_rejected():
    with pytest.raises(ValueError):
        find_matching_sentences("First sentence.", "Second sentence.", threshold=101)


def test_non_string_input_is_rejected():
    with pytest.raises(TypeError):
        find_matching_sentences(None, "Some sentence.")
