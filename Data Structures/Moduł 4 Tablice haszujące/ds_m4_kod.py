# Implementacja tablicy haszującej z łańcuchowaniem
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        if not self.table[index]:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next and current.key != key:
                current = current.next
            if current.key == key:
                current.value = value  # Aktualizacja wartości
            else:
                current.next = Node(key, value)

    def get(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        index = self._hash(key)
        current = self.table[index]
        if not current:
            return
        if current.key == key:
            self.table[index] = current.next
            return
        while current.next and current.next.key != key:
            current = current.next
        if current.next:
            current.next = current.next.next

# Testowanie tablicy haszującej
ht = HashTable()
ht.insert("apple", 5)
ht.insert("banana", 8)
ht.insert("orange", 3)
print("Wartość dla 'apple':", ht.get("apple"))  # Wyświetla: 5
print("Wartość dla 'banana':", ht.get("banana"))  # Wyświetla: 8
ht.remove("banana")
print("Wartość dla 'banana' po usunięciu:", ht.get("banana"))  # Wyświetla: None