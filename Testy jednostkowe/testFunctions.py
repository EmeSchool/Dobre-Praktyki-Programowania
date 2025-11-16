def is_palindrome(text: str) -> bool:
    # Zamieniamy wszystkie litery na małe i usuwamy białe znaki (spacje, taby, nowe linie)
    cleaned = ''.join(ch.lower() for ch in text if not ch.isspace())
    # Sprawdzamy, czy tekst jest równy swojej odwróconej wersji
    return cleaned == cleaned[::-1]


def fibonacci(n: int) -> int:
    # Sprawdzamy, czy argument jest nieujemny
    if n < 0:
        raise ValueError("n musi być liczbą nieujemną")

    # Inicjalizacja pierwszych dwóch liczb Fibonacciego
    a, b = 0, 1

    # Iteracyjnie przesuwamy parę liczb do przodu n razy
    for _ in range(n):
        a, b = b, a + b

    # a zawiera n-tą liczbę Fibonacciego
    return a


def count_vowels(text: str) -> int:
    # Zestaw samogłosek — używamy set dla szybkiego sprawdzania "in"
    vowels = set("aeiouy")
    # Zliczamy, ile znaków po zamianie na małe litery należy do zestawu samogłosek
    return sum(1 for ch in text.lower() if ch in vowels)


def calculate_discount(price: float, discount: float) -> float:
    # Sprawdzamy poprawność rabatu — musi być od 0 do 1
    if not (0 <= discount <= 1):
        raise ValueError("discount musi być w zakresie 0–1")
    # Liczymy cenę po uwzględnieniu rabatu
    return price * (1 - discount)


def flatten_list(nested_list: list) -> list:
    # Lista wynikowa ze spłaszczonymi elementami
    result = []

    # Iterujemy po wszystkich elementach listy
    for item in nested_list:
        # Jeśli element jest listą — spłaszczamy ją rekurencyjnie
        if isinstance(item, list):
            result.extend(flatten_list(item))
        # Jeśli nie — dodajemy zwykły element
        else:
            result.append(item)

    return result


import re

def word_frequencies(text: str) -> dict:
    # Usuwamy interpunkcję i dzielimy tekst na słowa (regex znajduje ciągi alfanumeryczne)
    words = re.findall(r'\b\w+\b', text.lower())

    # Tworzymy słownik z licznikami słów
    freq = {}
    for word in words:
        # get zwraca aktualną wartość lub 0, jeśli słowa nie ma w słowniku
        freq[word] = freq.get(word, 0) + 1

    return freq


def is_prime(n: int) -> bool:
    """
    Zwraca True, jeśli n jest liczbą pierwszą.
    Zgodnie z definicją:
        n < 2 → False
    """
    # Eliminujemy liczby < 2
    if n < 2:
        return False

    # 2 i 3 są pierwsze
    if n in (2, 3):
        return True

    # Eliminujemy liczby podzielne przez 2 lub 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Zaczynamy od 5 i badamy tylko liczby w formie 6k ± 1
    i = 5

    # Sprawdzamy tylko do pierwiastka z n
    while i * i <= n:
        # Jeśli n dzieli się przez i lub i+2 → nie jest pierwsze
        if n % i == 0 or n % (i + 2) == 0:
            return False

        # Przeskakujemy do kolejnych liczb 6k ± 1
        i += 6

    # Jeśli nie znaleziono dzielników — n jest pierwsze
    return True
