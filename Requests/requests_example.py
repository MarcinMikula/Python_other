import requests
from requests.exceptions import RequestException, HTTPError, Timeout

# Sztuczne API (nie istnieje, używamy do demonstracji)
BASE_URL = "https://fake-api.example.com"
USERS_URL = f"{BASE_URL}/users"
USER_URL = lambda user_id: f"{USERS_URL}/{user_id}"
UPLOAD_URL = f"{BASE_URL}/upload"
AUTH_URL = f"{BASE_URL}/auth"
COOKIES_URL = f"{BASE_URL}/cookies"


# 1. GET: Pobieranie listy użytkowników
def get_users():
    try:
        response = requests.get(USERS_URL, params={"limit": 10}, timeout=5)
        response.raise_for_status()
        users = response.json()
        print("Lista użytkowników:")
        for user in users.get("users", []):
            print(f"- {user['name']} (ID: {user['id']})")
        return users
    except HTTPError as e:
        print(f"Błąd HTTP: {e}")
    except Timeout:
        print("Przekroczono czas oczekiwania na odpowiedź")
    except RequestException as e:
        print(f"Błąd żądania: {e}")
    return None


# 2. POST: Dodanie nowego użytkownika
def create_user(name, email):
    headers = {"Content-Type": "application/json"}
    user_data = {"name": name, "email": email}
    try:
        response = requests.post(USERS_URL, json=user_data, headers=headers)
        response.raise_for_status()
        new_user = response.json()
        print(f"Utworzono użytkownika: {new_user['name']} (ID: {new_user['id']})")
        return new_user
    except HTTPError as e:
        print(f"Błąd HTTP: {e}")
    except RequestException as e:
        print(f"Błąd żądania: {e}")
    return None


# 3. PUT: Aktualizacja danych użytkownika
def update_user(user_id, new_name):
    headers = {"Content-Type": "application/json"}
    user_data = {"name": new_name}
    try:
        response = requests.put(USER_URL(user_id), json=user_data, headers=headers)
        response.raise_for_status()
        updated_user = response.json()
        print(f"Zaktualizowano użytkownika: {updated_user['name']} (ID: {updated_user['id']})")
        return updated_user
    except HTTPError as e:
        print(f"Błąd HTTP: {e}")
    except RequestException as e:
        print(f"Błąd żądania: {e}")
    return None


# 4. DELETE: Usunięcie użytkownika
def delete_user(user_id):
    try:
        response = requests.delete(USER_URL(user_id))
        response.raise_for_status()
        print(f"Usunięto użytkownika o ID: {user_id}")
        return True
    except HTTPError as e:
        print(f"Błąd HTTP: {e}")
    except RequestException as e:
        print(f"Błąd żądania: {e}")
    return False


# 5. Użycie sesji do wielu żądań
def session_example():
    session = requests.Session()
    session.headers.update({
        "Authorization": "Bearer fake-token",
        "Accept": "application/json"
    })

    try:
        response1 = session.get(USERS_URL, params={"limit": 5})
        response1.raise_for_status()
        print("Użytkownicy (z sesji):", response1.json())

        response2 = session.get(USER_URL(1))
        response2.raise_for_status()
        print("Szczegóły użytkownika (z sesji):", response2.json())
    except HTTPError as e:
        print(f"Błąd HTTP: {e}")
    except RequestException as e:
        print(f"Błąd żądania: {e}")


# 6. HEAD: Pobieranie nagłówków
def get_headers():
    try:
        response = requests.head(USERS_URL)
        print("Nagłówki odpowiedzi:")
        for key, value in response.headers.items():
            print(f"{key}: {value}")
    except RequestException as e:
        print(f"Błąd żądania: {e}")


# 7. OPTIONS: Sprawdzanie dozwolonych metod
def get_allowed_methods():
    try:
        response = requests.options(USERS_URL)
        allowed_methods = response.headers.get("Allow", "Brak informacji")
        print(f"Dozwolone metody: {allowed_methods}")
    except RequestException as e:
        print(f"Błąd żądania: {e}")


# 8. POST: Przesyłanie pliku
def upload_file(file_path):
    try:
        with open(file_path, "rb") as f:
            files = {"file": (file_path, f, "text/plain")}
            response = requests.post(UPLOAD_URL, files=files)
        response.raise_for_status()
        result = response.json()
        print(f"Plik przesłany: {result.get('filename')}")
        return result
    except FileNotFoundError:
        print(f"Plik {file_path} nie istnieje")
    except HTTPError as e:
        print(f"Błąd HTTP: {e}")
    except RequestException as e:
        print(f"Błąd żądania: {e}")
    return None


# 9. GET: Autoryzacja Basic Auth
def basic_auth_example():
    try:
        response = requests.get(AUTH_URL, auth=("fake-user", "fake-password"))
        response.raise_for_status()
        data = response.json()
        print("Dane z autoryzacją Basic Auth:", data)
        return data
    except HTTPError as e:
        print(f"Błąd HTTP: {e}")
    except RequestException as e:
        print(f"Błąd żądania: {e}")
    return None


# 10. GET/POST: Obsługa ciasteczek
def cookies_example():
    session = requests.Session()
    try:
        # Pierwsze żądanie: Ustawienie ciasteczka
        response1 = session.get(COOKIES_URL)
        response1.raise_for_status()
        print("Ciasteczka po pierwszym żądaniu:", session.cookies.get_dict())

        # Drugie żądanie: Wysłanie ciasteczka z powrotem
        response2 = session.post(COOKIES_URL, data={"action": "check"})
        response2.raise_for_status()
        result = response2.json()
        print("Odpowiedź z ciasteczkiem:", result)
        return result
    except HTTPError as e:
        print(f"Błąd HTTP: {e}")
    except RequestException as e:
        print(f"Błąd żądania: {e}")
    return None


# Główna funkcja
def main():
    print("=== Przykład 1: GET ===")
    get_users()

    print("\n=== Przykład 2: POST ===")
    create_user("Jan Kowalski", "jan@example.com")

    print("\n=== Przykład 3: PUT ===")
    update_user(1, "Jan Nowak")

    print("\n=== Przykład 4: DELETE ===")
    delete_user(1)

    print("\n=== Przykład 5: Sesja ===")
    session_example()

    print("\n=== Przykład 6: HEAD ===")
    get_headers()

    print("\n=== Przykład 7: OPTIONS ===")
    get_allowed_methods()

    print("\n=== Przykład 8: Przesyłanie pliku ===")
    upload_file("example.txt")

    print("\n=== Przykład 9: Basic Auth ===")
    basic_auth_example()

    print("\n=== Przykład 10: Ciasteczka ===")
    cookies_example()


if __name__ == "__main__":
    main()
