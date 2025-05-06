import pytest

from ejercicios.lps.lps_brute import solve_lps_brute



def test_simple_palindrome():
    # Una sola cadena que ya es palíndroma
    lines = ["racecar"]
    assert solve_lps_brute(lines) == ["racecar"]


def test_header_parsing():
    # Primera línea como número de cadenas
    lines = ["2", "Madam", "Hello"]
    # "Madam" normalizado -> "madam"; "Hello" -> "hello"
    assert solve_lps_brute(lines) == ["madam", "ll"]


def test_punctuation_and_case():
    # Ignora puntuación y mayúsculas
    lines = ["A man, a plan, a canal: Panama!"]
    # Normalizado -> "amanaplanacanalpanama"
    assert solve_lps_brute(lines) == ["amanaplanacanalpanama"]


def test_multiple_strings_no_header():
    # Sin encabezado numérico, interpreta todas las líneas como cadenas
    lines = ["Abba", "xyz"]
    assert solve_lps_brute(lines) == ["abba", "x"]


def test_empty_and_single():
    # Cadena vacía y cadena de un solo carácter
    lines = ["", "x"]
    assert solve_lps_brute(lines) == ["", "x"]


def test_long_string_substring():
    # Caso con palíndromo en parte de la cadena
    lines = ["abacdfgdcaba"]
    # El primer palíndromo más largo encontrado es "aba"
    assert solve_lps_brute(lines) == ["aba"]

if __name__ == "__main__":
    pytest.main()
