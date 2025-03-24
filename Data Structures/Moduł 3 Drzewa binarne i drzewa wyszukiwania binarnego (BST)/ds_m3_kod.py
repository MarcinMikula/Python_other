# Implementacja drzewa wyszukiwania binarnego (BST)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

# Testowanie BST
bst = BST()
values = [50, 30, 70, 20, 40, 60, 80]
for value in values:
    bst.insert(value)
print("Przechodzenie inorder:", bst.inorder())  # Wyświetla: [20, 30, 40, 50, 60, 70, 80]
print("Wyszukiwanie 40:", "Znaleziono" if bst.search(40) else "Nie znaleziono")  # Wyświetla: Znaleziono
print("Wyszukiwanie 90:", "Znaleziono" if bst.search(90) else "Nie znaleziono")  # Wyświetla: Nie znaleziono