import func
import pytest

LETTER = 'x'
SECRET_WORD = 'text'
GAMER_WORD = ['_ '] * len(SECRET_WORD)


def test_letter_found_empty():
    letter = ""
    secret_word = ""
    gamer_word = ""
    test_empty = func.letter_found(letter, secret_word, gamer_word)
    assert test_empty == ""

def test_letter_found_not_empty():
    letter = LETTER
    secret_word = SECRET_WORD
    gamer_word = GAMER_WORD
    not_empty = func.letter_found(letter, secret_word, gamer_word)
    assert not_empty == gamer_word