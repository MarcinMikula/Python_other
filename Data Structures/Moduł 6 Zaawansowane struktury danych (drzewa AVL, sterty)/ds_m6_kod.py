# Implementacja sterty minimalnej (Min Heap)
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, i):
        parent = self.parent(i)
        while i > 0 and self.heap[parent] > self.heap[i]:
            self.swap(i, parent)
            i = parent
            parent = self.parent(i)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return min_val

    def _sift_down(self, i):
        min_index = i
        size = len(self.heap)
        while True:
            left = self.left_child(i)
            right = self.right_child(i)
            if left < size and self.heap[left] < self.heap[min_index]:
                min_index = left
            if right < size and self.heap[right] < self.heap[min_index]:
                min_index = right
            if i != min_index:
                self.swap(i, min_index)
                i = min_index
            else:
                break

# Testowanie sterty minimalnej
heap = MinHeap()
values = [5, 3, 7, 1, 4, 2]
for value in values:
    heap.insert(value)
print("Sterta po wstawieniu:", heap.heap)  # Wyświetla: [1, 3, 2, 5, 4, 7]
print("Minimum:", heap.extract_min())  # Wyświetla: 1
print("Sterta po usunięciu minimum:", heap.heap)  # Wyświetla: [2, 3, 7, 5, 4]