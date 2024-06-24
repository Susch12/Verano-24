import random
import time 
class BinaryHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while parent_index >= 0 and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index
            parent_index = (index - 1) // 2

    def get_min(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def delete_min(self):
        if self.is_empty():
            return None

        min_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)

        return min_value

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)


# Example Usage
heap = BinaryHeap()

# Insert elements
with open("datos.txt", "w") as file:
    for i in range(200):
        heap = BinaryHeap()
        tiempos_insert = []
        tiempos_get_min = []
        tiempos_delete_min = []

        # Insertar 6 elementos aleatorios y medir el tiempo de inserción
        for _ in range(6):
            valor = random.randint(1, 100)
            inicio_insert = time.time()
            heap.insert(valor)
            fin_insert = time.time()
            tiempos_insert.append(fin_insert - inicio_insert)

        # Medir el tiempo para obtener el mínimo
        inicio_get_min = time.time()
        min_element = heap.get_min()
        fin_get_min = time.time()
        tiempos_get_min.append(fin_get_min - inicio_get_min)

        # Medir el tiempo para eliminar el mínimo
        inicio_delete_min = time.time()
        deleted_min = heap.delete_min()
        fin_delete_min = time.time()
        tiempos_delete_min.append(fin_delete_min - inicio_delete_min)

        # Medir el tiempo para obtener el nuevo mínimo
        inicio_get_min = time.time()
        new_min = heap.get_min()
        fin_get_min = time.time()
        tiempos_get_min.append(fin_get_min - inicio_get_min)

        file.write(f"Ejecución {i + 1}:\n")
        file.write(f"Elemento mínimo inicial: {min_element}\n")
        file.write(f"Elemento mínimo eliminado: {deleted_min}\n")
        file.write(f"Nuevo elemento mínimo: {new_min}\n")
        file.write(f"Tiempos de inserción: {tiempos_insert}\n")
        file.write(f"Tiempos de get_min: {tiempos_get_min}\n")
        file.write(f"Tiempos de delete_min: {tiempos_delete_min}\n\n")
