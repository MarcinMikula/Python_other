# Requests Library Examples

Ten projekt zawiera przykłady użycia biblioteki `requests` w Pythonie, demonstrując różne scenariusze pracy z API.

## Opis projektu

### Allegro Categories Fetcher
Pierwsza część projektu (`allegro_categories.py`) pokazuje, jak używać biblioteki `requests` do pobierania listy kategorii z Allegro REST API. Kod demonstruje:
- Uzyskiwanie tokena OAuth za pomocą przepływu `client_credentials`.
- Wykonywanie żądania GET do endpointu `/sale/categories`.
- Obsługę błędów i przetwarzanie odpowiedzi JSON.

### Requests Examples
Druga część projektu (`requests_example.py`) zawiera szczegółowe przykłady użycia biblioteki `requests` z użyciem sztucznego API (`https://fake-api.example.com`). Pokazuje różne metody HTTP i funkcje, w tym:
- Metody HTTP: GET, POST, PUT, DELETE, HEAD, OPTIONS.
- Użycie sesji (`requests.Session()`).
- Przesyłanie plików (`files`).
- Autoryzacja Basic Auth (`auth`).
- Obsługa ciasteczek.
- Obsługa błędów (np. timeout, HTTPError).

### Lotto API Examples
Trzecia część projektu zawiera przykłady pracy z Lotto API:
- `lotto_info.py`: Pobieranie informacji o loteriach za pomocą endpointu `/api/open/v1/lotteries/info`.
- `lotto_draw_results.py`: Pobieranie wyników losowań dla określonej daty za pomocą endpointu `/api/open/v1/lotteries/draw-results/by-date`.

## Wymagania
- Python 3.6+
- Biblioteka `requests` (`pip install requests`)
- Dla `allegro_categories.py`: Dane dostępowe do Allegro API (Client ID i Client Secret) – zarejestruj aplikację na https://apps.developer.allegro.pl.allegrosandbox.pl.
- Dla `lotto_info.py` i `lotto_draw_results.py`: Klucz API do Lotto API – zarejestruj aplikację na https://developers.lotto.pl/.

## Instalacja
1. Sklonuj repozytorium:
   ```bash
   git clone <adres-repozytorium>
   cd <nazwa-repozytorium>