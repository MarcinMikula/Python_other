# Operacje na listach w stylu funkcyjnym/proceduralnym
from array import array

# Funkcje do operacji na listach
def add_elements(lst, elements):
    lst.extend(elements)
    return lst

def remove_element(lst, element):
    if element in lst:
        lst.remove(element)
    return lst

def insert_at_index(lst, index, element):
    lst.insert(index, element)
    return lst

def sort_list(lst):
    return sorted(lst)  # Funkcyjny styl – zwracamy nową listę

def reverse_list(lst):
    return list(reversed(lst))  # Funkcyjny styl – zwracamy nową listę

# Użycie listy jako stosu (LIFO)
def stack_operations():
    stack = []
    stack.append(1)  # push
    stack.append(2)
    stack.append(3)
    popped = stack.pop()  # pop
    return stack, popped

# Użycie listy jako kolejki (FIFO)
def queue_operations():
    queue = []
    queue.append("A")  # enqueue
    queue.append("B")
    queue.append("C")
    dequeued = queue.pop(0)  # dequeue
    return queue, dequeued

# List comprehensions w stylu funkcyjnym
def square_numbers(numbers):
    return [x * x for x in numbers]

# Użycie tablicy (moduł array)
def array_example():
    arr = array('i', [1, 2, 3, 4])  # Tablica liczb całkowitych
    arr.append(5)
    return list(arr)

# Testowanie operacji
lst = [1, 2, 3]
print("Oryginalna lista:", lst)
print("Po dodaniu [4, 5]:", add_elements(lst, [4, 5]))
print("Po usunięciu 3:", remove_element(lst, 3))
print("Po wstawieniu 0 na indeks 0:", insert_at_index(lst, 0, 0))
print("Posortowana lista:", sort_list(lst))
print("Odwrócona lista:", reverse_list(lst))

stack, popped = stack_operations()
print("Stos po operacjach:", stack, "Usunięty element:", popped)

queue, dequeued = queue_operations()
print("Kolejka po operacjach:", queue, "Usunięty element:", dequeued)

numbers = [1, 2, 3, 4]
print("Kwadraty liczb:", square_numbers(numbers))

print("Tablica (array):", array_example())