import pytest
from scripts.style_guide_builder import analyze_text

def test_analyze_text_basic():
    text = "The quick brown fox jumps over the lazy dog. It was a very sunny day!"
    analysis = analyze_text(text)

    # Words > 4 letters in lowercase: quick, brown, jumps, sunny
    assert "quick" in analysis['top_nouns_and_verbs']
    assert "brown" in analysis['top_nouns_and_verbs']
    assert "jumps" in analysis['top_nouns_and_verbs']
    assert "sunny" in analysis['top_nouns_and_verbs']

    # Words <= 4 letters should be excluded
    assert "over" not in analysis['top_nouns_and_verbs']
    assert "lazy" not in analysis['top_nouns_and_verbs']
    assert "very" not in analysis['top_nouns_and_verbs']

    # Sentence analysis:
    # S1: "The quick brown fox jumps over the lazy dog" -> 9 words
    # S2: "It was a very sunny day" -> 6 words
    # Average: (9 + 6) / 2 = 7.5
    assert analysis['word_count'] == 15
    assert analysis['sentence_count'] == 2
    assert analysis['avg_sentence_length'] == 7.5
    assert analysis['max_sentence_length'] == 9
    assert analysis['min_sentence_length'] == 6

def test_analyze_text_empty():
    analysis = analyze_text("")
    assert analysis['top_nouns_and_verbs'] == []
    assert analysis['word_count'] == 0
    assert analysis['sentence_count'] == 0
    assert analysis['avg_sentence_length'] == 0
    assert analysis['max_sentence_length'] == 0
    assert analysis['min_sentence_length'] == 0

def test_analyze_text_short_words_only():
    text = "The cat sat on a mat."
    analysis = analyze_text(text)
    # All words <= 4 letters
    assert analysis['top_nouns_and_verbs'] == []
    # "The", "cat", "sat", "on", "a", "mat" -> 6 words
    assert analysis['word_count'] == 6
    assert analysis['sentence_count'] == 1
    assert analysis['avg_sentence_length'] == 6.0

def test_analyze_text_multiple_punctuation():
    text = "Wait!!! Stop... Go?"
    analysis = analyze_text(text)
    # Sentences: "Wait", "Stop", "Go"
    # Each is 1 word
    assert analysis['word_count'] == 3
    assert analysis['sentence_count'] == 3
    assert analysis['avg_sentence_length'] == 1.0
    assert analysis['max_sentence_length'] == 1
    assert analysis['min_sentence_length'] == 1

def test_analyze_text_word_frequency():
    text = "Apple apple apple banana banana cherry"
    analysis = analyze_text(text)
    # apple (5) - freq 3
    # banana (6) - freq 2
    # cherry (6) - freq 1
    # Note: re.findall(r'\b[A-Za-z]+\b', text.lower()) will find them

    assert analysis['top_nouns_and_verbs'][0] == "apple"
    assert analysis['top_nouns_and_verbs'][1] == "banana"
    assert analysis['top_nouns_and_verbs'][2] == "cherry"
