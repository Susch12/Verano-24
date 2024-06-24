class SkewHeap:
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def merge(self, h1, h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1
        if h1.key > h2.key:
            h1, h2 = h2, h1
        h1.right, h1.left = h1.left, self.merge(h1.right, h2)
        return h1

    def insert(self, key):
        new_node = self.Node(key)
        self.root = self.merge(self.root, new_node)

    def delete_min(self):
        if self.root is None:
            return None
        min_elem = self.root.key
        self.root = self.merge(self.root.left, self.root.right)
        return min_elem
