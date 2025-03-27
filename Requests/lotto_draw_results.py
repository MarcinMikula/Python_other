# Zabawa w API Lotto, hazard to zuo a zwłaszcza taki w którym szanse na wygraną są bliskie zera

import requests
from requests.exceptions import RequestException, HTTPError
from datetime import datetime

# Dane dostępowe (zastąp swoim kluczem API)
API_KEY = "twoj_klucz_api"
DRAW_RESULTS_URL = "https://developers.lotto.pl/api/open/v1/lotteries/draw-results/by-date"

# Funkcja do pobierania wyników losowań dla określonej daty
def get_draw_results(draw_date):
    headers = {
        "X-API-Key": API_KEY
    }
    # Konwersja daty na format ISO 8601 (jeśli nie jest w odpowiednim formacie)
    try:
        if isinstance(draw_date, str):
            # Parsujemy datę, aby upewnić się, że jest w formacie ISO 8601
            parsed_date = datetime.fromisoformat(draw_date.replace("Z", "+00:00"))
        else:
            parsed_date = draw_date
        formatted_date = parsed_date.strftime("%Y-%m-%dT%H:%M:%SZ")
    except ValueError as e:
        print(f"Błąd formatu daty: {e}. Oczekiwano formatu YYYY-MM-DDThh:mm:ssZ, np. 2019-08-24T14:15:22Z")
        return None

    params = {
        "drawDate": formatted_date
    }

    try:
        response = requests.get(DRAW_RESULTS_URL, headers=headers, params=params)
        response.raise_for_status()
        results = response.json()
        if not results:
            print(f"Brak wyników dla daty {formatted_date}")
            return None

        print(f"Wyniki losowań dla daty {formatted_date}:")
        for result in results:
            print(f"- Typ gry: {result['gameType']}")
            print(f"  ID losowania: {result['drawSystemId']}")
            print(f"  Data losowania: {result['drawDate']}")
            print(f"  Wyniki: {result['results']}")
            print(f"  Specjalne wyniki: {result['showSpecialResults']}")
            print(f"  Nowy Eurojackpot: {result['isNewEurojackpotDraw']}")
        return results
    except HTTPError as e:
        if response.status_code == 401:
            print("Błąd 401: Klient nieautoryzowany. Sprawdź klucz API.")
        elif response.status_code == 404:
            print(f"Błąd 404: Nie znaleziono wyników dla daty {formatted_date}")
        else:
            print(f"Błąd HTTP: {e}")
    except RequestException as e:
        print(f"Błąd żądania: {e}")
    return None

# Główna funkcja
def main():
    # Przykład daty w formacie ISO 8601
    draw_date = "2019-08-24T14:15:22Z"
    get_draw_results(draw_date)

if __name__ == "__main__":
    main()