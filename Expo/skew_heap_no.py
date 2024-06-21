class SkewHeap:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @staticmethod
    def empty():
        return SkewHeap()

    @staticmethod
    def singleton(x):
        return SkewHeap(x, SkewHeap.empty(), SkewHeap.empty())

    @staticmethod
    def union(heap1, heap2):
        if heap1.value is None:
            return heap2
        if heap2.value is None:
            return heap1

        if heap1.value <= heap2.value:
            return SkewHeap(heap1.value, SkewHeap.union(heap2, heap1.right), heap1.left)
        else:
            return SkewHeap(heap2.value, SkewHeap.union(heap1, heap2.right), heap2.left)

    def insert(self, x):
        return SkewHeap.union(SkewHeap.singleton(x), self)

    def extract_min(self):
        if self.value is None:
            return None
        return (self.value, SkewHeap.union(self.left, self.right))

# Example usage:
heap = SkewHeap.empty()
heap = heap.insert(3)
heap = heap.insert(1)
heap = heap.insert(4)
min_elem, new_heap = heap.extract_min()

print(f"Minimum element: {min_elem}")
