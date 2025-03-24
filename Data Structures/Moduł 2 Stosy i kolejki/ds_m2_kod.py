# Implementacja stosu za pomocą listy jednokierunkowej
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        if not self.top:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

# Implementacja kolejki za pomocą listy jednokierunkowej
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None
        dequeued = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return dequeued

    def front_element(self):
        if not self.front:
            return None
        return self.front.data

    def is_empty(self):
        return self.front is None

# Testowanie stosu i kolejki
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stos po push:", stack.peek())  # Wyświetla: 3
print("Pop ze stosu:", stack.pop())  # Wyświetla: 3
print("Stos po pop:", stack.peek())  # Wyświetla: 2

queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
print("Kolejka po enqueue:", queue.front_element())  # Wyświetla: A
print("Dequeue z kolejki:", queue.dequeue())  # Wyświetla: A
print("Kolejka po dequeue:", queue.front_element())  # Wyświetla: B