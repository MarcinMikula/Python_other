import pytest
import sys
import os
import warnings
from unittest.mock import patch

# Funkcje do przetestowania
def add(a, b):
    return a + b

def divide(a, b):
    return a / b

def save_result_to_file(result, filename):
    with open(filename, "w") as f:
        f.write(str(result))

def api_add_endpoint(a, b):
    return {"result": add(a, b)}

def call_external_api(a, b):
    result = add(a, b)
    print("Wynik API:", result)
    return result

# Fixture do przygotowania danych
@pytest.fixture
def sample_data():
    return {"a": 2, "b": 3}

# Fixture do tymczasowego pliku
@pytest.fixture
def temp_file():
    filename = "temp_result.txt"
    yield filename
    if os.path.exists(filename):
        os.remove(filename)

# 1. Test jednostkowy
def test_add_unit():
    assert add(2, 3) == 5, "Dodawanie 2 + 3 powinno dać 5"

# 2. Test integracyjny
@pytest.mark.integration
def test_add_and_save(temp_file):
    result = add(2, 3)
    save_result_to_file(result, temp_file)
    with open(temp_file, "r") as f:
        saved_result = int(f.read())
    assert saved_result == 5, "Zapisany wynik powinien być 5"

# 3. Test funkcjonalny
@pytest.mark.functional
def test_api_add_endpoint():
    response = api_add_endpoint(2, 3)
    assert response["result"] == 5, "API powinno zwrócić wynik 5"

# 4. Test parametryzowany
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (0, 5, 5),
    (-1, 1, 0),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected, f"Dodawanie {a} + {b} powinno dać {expected}"

# 5. Test wyjątków
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

# 6. Test z mockowaniem
@patch("builtins.print")
def test_call_external_api(mock_print):
    result = call_external_api(2, 3)
    mock_print.assert_called_with("Wynik API:", result)
    assert result == 5, "Wynik API powinien być 5"

# 7. Test z użyciem fixture
def test_add_with_fixture(sample_data):
    result = add(sample_data["a"], sample_data["b"])
    assert result == 5, "Dodawanie z fixture powinno dać 5"

# 8. Test z markerem
@pytest.mark.slow
def test_add_slow():
    assert add(1000, 2000) == 3000, "Test oznaczony jako 'slow'"

# 9. Test z pomijaniem
@pytest.mark.skipif(sys.version_info < (3, 8), reason="Wymaga Pythona 3.8 lub nowszego")
def test_skipif_python_version():
    assert True, "Test działa tylko na Pythonie 3.8+"

# 10. Test z oczekiwanym niepowodzeniem
@pytest.mark.xfail(reason="Oczekiwane niepowodzenie, bo funkcja ma błąd")
def test_add_expected_failure():
    assert add(3, 3) == 7, "Ten test powinien nie przejść"

# 11. Test z przechwytywaniem wyjścia
def test_print_output(capsys):
    print("To jest testowe wyjście")
    captured = capsys.readouterr()
    assert captured.out == "To jest testowe wyjście\n", "Wyjście powinno być poprawne"

# 12. Test z tymczasowym plikiem
def test_write_to_tmp_path(tmp_path):
    file = tmp_path / "test_file.txt"
    file.write_text("Dane w tmp_path")
    assert file.read_text() == "Dane w tmp_path", "Zawartość pliku w tmp_path powinna być poprawna"

# 13. Test z ostrzeżeniami
def test_warning():
    with pytest.warns(UserWarning):
        warnings.warn("To jest ostrzeżenie", UserWarning)