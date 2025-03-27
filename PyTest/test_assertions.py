import pytest
import warnings  # Dodajemy import warnings

# Funkcja do przetestowania
def calculate_discount(price, discount_percent):
    if price < 0 or discount_percent < 0 or discount_percent > 100:
        raise ValueError("Cena i procent rabatu muszą być nieujemne, a rabat <= 100")
    if discount_percent > 50:  # Dodajemy ostrzeżenie dla dużego rabatu
        warnings.warn("Rabat większy niż 50% - to może być pomyłka", UserWarning)
    discount = price * (discount_percent / 100)
    return price - discount

# 1. Podstawowa asercja: Sprawdzanie wartości liczbowej
def test_calculate_discount_basic():
    result = calculate_discount(100, 20)
    assert result == 80, "Rabat 20% na 100 powinien dać 80"

# 2. Asercja z porównaniem liczb zmiennoprzecinkowych (użycie pytest.approx)
def test_calculate_discount_float():
    result = calculate_discount(100, 15)
    assert result == pytest.approx(85.0), "Rabat 15% na 100 powinien dać 85 (z tolerancją)"

# 3. Asercja z wyjątkiem (pytest.raises)
def test_calculate_discount_negative_price():
    with pytest.raises(ValueError) as exc_info:
        calculate_discount(-100, 20)
    assert "Cena i procent rabatu muszą być nieujemne" in str(exc_info.value), "Oczekiwano błędu o nieujemnej cenie"

# 4. Asercja z listą
def test_calculate_discount_multiple_values():
    results = [calculate_discount(price, 10) for price in [100, 200, 300]]
    assert results == [90, 180, 270], "Rabaty 10% na ceny [100, 200, 300] powinny dać [90, 180, 270]"

# 5. Asercja z słownikiem
def test_calculate_discount_dict():
    prices = {"item1": 100, "item2": 200}
    expected = {"item1": 90, "item2": 180}
    results = {item: calculate_discount(price, 10) for item, price in prices.items()}
    assert results == expected, "Rabaty 10% na słownik cen powinny dać oczekiwane wartości"

# 6. Asercja z warunkiem logicznym
def test_calculate_discount_zero_discount():
    result = calculate_discount(100, 0)
    assert result == 100, "Rabat 0% na 100 powinien dać 100"

# 7. Asercja z ciągiem znaków (poprawiona)
def test_calculate_discount_string_representation():
    result = calculate_discount(100, 20)
    assert str(int(result)) == "80", "Stringowa reprezentacja wyniku powinna być '80'"  # Konwertujemy na int, aby usunąć .0

# 8. Asercja z None
def test_calculate_discount_none_check():
    result = calculate_discount(100, 20)
    assert result is not None, "Wynik nie powinien być None"

# 9. Asercja z porównaniem podzbioru (użycie in)
def test_calculate_discount_in_list():
    result = calculate_discount(100, 20)
    assert result in [80, 90, 100], "Wynik powinien być w liście [80, 90, 100]"

# 10. Asercja z ostrzeżeniem (poprawiona)
def test_calculate_discount_warning():
    with pytest.warns(UserWarning):
        result = calculate_discount(100, 75)  # Rabat > 50%, więc powinno wygenerować ostrzeżenie
    assert result == 25, "Rabat 75% na 100 powinien dać 25"

# 11. Asercja celowo niepoprawna (oznaczona jako xfail)
@pytest.mark.xfail(reason="Ten test celowo nie przejdzie")
def test_calculate_discount_fail():
    result = calculate_discount(100, 20)
    assert result == 90, "Ten test celowo nie przejdzie (oczekiwano 90, a powinno być 80)"
