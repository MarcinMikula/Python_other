# Szkolenie Pytest: Przewodnik po frameworku

Szkolenie oparte na dokumentacji pytest (https://docs.pytest.org/). Przewodnik po praktycznych aspektach używania pytest do testowania w Pythonie, rozszerzony o przykłady metod i funkcji.

## Struktura repozytorium

- `pytest_streszczenie.txt`: Streszczenie kluczowych funkcji pytest.
- `test_pytest_example.py`: Przykładowy kod z testami w pytest, rozszerzony o metody i funkcje.
- `pytest_wyjasnienie.txt`: Wyjaśnienie kodu krok po kroku, uwzględniające nowe przykłady.

## Zadania

- `pytest_zadania.txt`: Zadania do przećwiczenia funkcji pytest (5 zadań).

## Uruchomienie testów

1. Zainstaluj pytest: `pip install pytest`
2. Uruchom testy:
   - Wszystkie testy: `pytest test_pytest_example.py -v`
   - Testy z markerem "slow": `pytest test_pytest_example.py -m slow`
   - Testy z debugowaniem: `pytest test_pytest_example.py --pdb`
   - Testy pasujące do "add": `pytest test_pytest_example.py -k "add"`
