class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class SkewHeap:
    def __init__(self):
        self.root = None

    def merge(self, h1, h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1
        if h1.key > h2.key:
            h1, h2 = h2, h1
        
        h1.right = self.merge(h1.right, h2)
        h1.left, h1.right = h1.right, h1.left
        
        return h1

    def insert(self, key):
        new_node = Node(key)
        self.root = self.merge(self.root, new_node)

    def delete_min(self):
        if self.root is None:
            return None
        min_key = self.root.key
        self.root = self.merge(self.root.left, self.root.right)
        return min_key

# Ejemplo de uso:
heap = SkewHeap()
heap.insert(10)
heap.insert(5)
heap.insert(20)
heap.insert(3)

print(heap.delete_min())  # Salida: 3
print(heap.delete_min())  # Salida: 5
print(heap.delete_min())  # Salida: 10
print(heap.delete_min())  # Salida: 20

