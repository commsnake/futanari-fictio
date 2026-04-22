import pytest
from scripts.generate_kdp_metadata import generate_blurb, generate_keywords

def test_generate_blurb():
    title = "The Maiden's Mast"
    tropes = ["Size Difference", "Blue Collar", "[Genre/Theme]"]
    subgenre = "Contemporary"

    blurb = generate_blurb(title, tropes, subgenre)

    assert f"**{title}**" in blurb
    assert f"A thrilling {subgenre} romance" in blurb
    assert "Size Difference, Blue Collar, [Genre/Theme]" in blurb
    assert "Warning: This book contains explicit content" in blurb
    assert "consensual non-consent" in blurb
    assert "18+ only" in blurb

def test_generate_keywords():
    tropes = ["Size Difference", "Blue Collar", "[Genre/Theme]", "Mpreg", "Enemies to Lovers"]
    subgenre = "Contemporary"

    keywords = generate_keywords(tropes, subgenre)

    assert len(keywords) <= 7
    assert "contemporary" in keywords
    assert "romance" in keywords
    assert "size difference" in keywords
    assert "blue collar" in keywords
    assert all(kw == kw.lower() for kw in keywords)

def test_generate_keywords_max_7():
    tropes = ["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8"]
    subgenre = "Sub"

    keywords = generate_keywords(tropes, subgenre)
    assert len(keywords) == 7

def test_generate_blurb_empty_tropes():
    blurb = generate_blurb("Title", [], "Sub")
    assert "featuring: ." in blurb

def test_generate_keywords_no_tropes():
    keywords = generate_keywords([], "Sub")
    assert len(keywords) == 5
    assert keywords == ["sub", "romance", "steamy", "explicit", "erotica"]
