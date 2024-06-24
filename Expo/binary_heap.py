class BinaryHeap:
    def __init__(self):
        self.data = []

    def insert(self, key):
        self.data.append(key)
        self._bubble_up(len(self.data) - 1)

    def delete_min(self):
        if len(self.data) == 0:
            return None
        self._swap(0, len(self.data) - 1)
        min_elem = self.data.pop()
        self._bubble_down(0)
        return min_elem

    def _bubble_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.data[index] < self.data[parent]:
            self._swap(index, parent)
            self._bubble_up(parent)

    def _bubble_down(self, index):
        child = 2 * index + 1
        if child >= len(self.data):
            return
        if child + 1 < len(self.data) and self.data[child + 1] < self.data[child]:
            child += 1
        if self.data[index] > self.data[child]:
            self._swap(index, child)
            self._bubble_down(child)

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
