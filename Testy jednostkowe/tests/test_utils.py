import pytest
from testFunctions import (
    is_palindrome,
    fibonacci,
    count_vowels,
    calculate_discount,
    flatten_list,
    word_frequencies,
    is_prime
)


# 1. is_palindrome -------------------------------------------------------------

def test_is_palindrome_basic():
    assert is_palindrome("kajak") is True
    assert is_palindrome("Kobyła ma mały bok") is True
    assert is_palindrome("python") is False


def test_is_palindrome_edge_cases():
    assert is_palindrome("") is True          # pusty string
    assert is_palindrome("A") is True         # pojedynczy znak


# 2. fibonacci -----------------------------------------------------------------

def test_fibonacci_values():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55


def test_fibonacci_invalid():
    with pytest.raises(ValueError):
        fibonacci(-1)


# 3. count_vowels --------------------------------------------------------------

def test_count_vowels_basic():
    assert count_vowels("Python") == 1
    assert count_vowels("AEIOUY") == 6
    assert count_vowels("bcd") == 0
    assert count_vowels("") == 0


def test_count_vowels_polish():
    # jeśli nie chcesz polskich znaków — zmień test
    assert count_vowels("Próba żółwia") == 4


# 4. calculate_discount --------------------------------------------------------

def test_calculate_discount_valid():
    assert calculate_discount(100, 0.2) == 80.0
    assert calculate_discount(50, 0) == 50.0
    assert calculate_discount(200, 1) == 0.0


def test_calculate_discount_invalid():
    with pytest.raises(ValueError):
        calculate_discount(100, -0.1)

    with pytest.raises(ValueError):
        calculate_discount(100, 1.5)


# 5. flatten_list --------------------------------------------------------------

def test_flatten_list_basic():
    assert flatten_list([1, 2, 3]) == [1, 2, 3]
    assert flatten_list([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]
    assert flatten_list([]) == []
    assert flatten_list([[[1]]]) == [1]
    assert flatten_list([1, [2, [3, [4]]]]) == [1, 2, 3, 4]


# 6. word_frequencies ----------------------------------------------------------

def test_word_frequencies_basic():
    assert word_frequencies("To be or not to be") == {
        "to": 2,
        "be": 2,
        "or": 1,
        "not": 1
    }


def test_word_frequencies_repeated():
    assert word_frequencies("Hello, hello!") == {"hello": 2}


def test_word_frequencies_empty():
    assert word_frequencies("") == {}


def test_word_frequencies_case_insensitive():
    assert word_frequencies("Python Python python") == {"python": 3}


def test_word_frequencies_polish_sentence():
    assert word_frequencies("Ala ma kota, a kot ma Ale.") == {
        "ala": 1,
        "ma": 2,
        "kota": 1,
        "a": 1,
        "kot": 1,
        "ale": 1
    }


# 7. is_prime ------------------------------------------------------------------

def test_is_prime_values():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(5) is True    # W TWOJEJ LIŚCIE BYŁO False, ale to BŁĄD — 5 JEST PIERWSZA
    assert is_prime(97) is True
