import time 
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insertar(self, clave):
        self.heap.append(clave)
        self._flotar(len(self.heap) - 1)

    def extraer_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._hundir(0)
        return max_val

    def _flotar(self, indice):
        padre = (indice - 1) // 2
        if indice > 0 and self.heap[indice] > self.heap[padre]:
            self.heap[indice], self.heap[padre] = self.heap[padre], self.heap[indice]
            self._flotar(padre)

    def _hundir(self, indice):
        mayor = indice
        izquierdo = 2 * indice + 1
        derecho = 2 * indice + 2
        if izquierdo < len(self.heap) and self.heap[izquierdo] > self.heap[mayor]:
            mayor = izquierdo
        if derecho < len(self.heap) and self.heap[derecho] > self.heap[mayor]:
            mayor = derecho
        if mayor != indice:
            self.heap[indice], self.heap[mayor] = self.heap[mayor], self.heap[indice]
            self._hundir(mayor)
class NodoBinomial:
    def __init__(self, clave):
        self.clave = clave
        self.padre = None
        self.hijo = None
        self.hermano = None
        self.grado = 0

class HeapBinomial:
    def __init__(self):
        self.cabeza = None

    def insertar(self, clave):
        nuevo_nodo = NodoBinomial(clave)
        nuevo_heap = HeapBinomial()
        nuevo_heap.cabeza = nuevo_nodo
        self.cabeza = self._unir(self.cabeza, nuevo_heap.cabeza)

    def extraer_min(self):
        if self.cabeza is None:
            return None
        min_nodo_padre = None
        min_nodo = self.cabeza
        actual = self.cabeza
        actual_padre = None

        while actual.hermano is not None:
            if actual.hermano.clave < min_nodo.clave:
                min_nodo = actual.hermano
                min_nodo_padre = actual
            actual = actual.hermano

        if min_nodo_padre is None:
            self.cabeza = min_nodo.hermano
        else:
            min_nodo_padre.hermano = min_nodo.hermano

        hijo = min_nodo.hijo
        temp_cabeza = None
        while hijo is not None:
            siguiente_hijo = hijo.hermano
            hijo.hermano = temp_cabeza
            temp_cabeza = hijo
            hijo = siguiente_hijo

        nuevo_heap = HeapBinomial()
        nuevo_heap.cabeza = temp_cabeza
        self.cabeza = self._unir(self.cabeza, nuevo_heap.cabeza)
        return min_nodo.clave

    def _mezclar(self, h1, h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1

        if h1.grado <= h2.grado:
            cabeza = h1
            h1 = h1.hermano
        else:
            cabeza = h2
            h2 = h2.hermano

        actual = cabeza

        while h1 is not None and h2 is not None:
            if h1.grado <= h2.grado:
                actual.hermano = h1
                h1 = h1.hermano
            else:
                actual.hermano = h2
                h2 = h2.hermano
            actual = actual.hermano

        if h1 is not None:
            actual.hermano = h1
        else:
            actual.hermano = h2

        return cabeza

    def _unir(self, h1, h2):
        if h1 is None:
            return h2
        if h2 is None:
            return h1

        cabeza = self._mezclar(h1, h2)
        if cabeza is None:
            return None

        anterior = None
        actual = cabeza
        siguiente = actual.hermano

        while siguiente is not None:
            if (actual.grado != siguiente.grado) or (siguiente.hermano is not None and siguiente.hermano.grado == actual.grado):
                anterior = actual
                actual = siguiente
            else:
                if actual.clave <= siguiente.clave:
                    actual.hermano = siguiente.hermano
                    self._enlazar(actual, siguiente)
                else:
                    if anterior is None:
                        cabeza = siguiente
                    else:
                        anterior.hermano = siguiente
                    self._enlazar(siguiente, actual)
                    actual = siguiente
            siguiente = actual.hermano

        return cabeza

    def _enlazar(self, padre, hijo):
        hijo.padre = padre
        hijo.hermano = padre.hijo
        padre.hijo = hijo
        padre.grado += 1

# Ejemplo de uso:
heap_binomial = HeapBinomial()
heap_binomial.insertar(10)
heap_binomial.insertar(5)
heap_binomial.insertar(20)
heap_binomial.insertar(1)

print(heap_binomial.extraer_min())  # Salida: 1
print(heap_binomial.extraer_min())  # Salida: 5
print(heap_binomial.extraer_min())  # Salida: 10
print(heap_binomial.extraer_min())  # Salida: 20
# Ejemplo de uso:
max_heap = MaxHeap()
max_heap.insertar(10)
max_heap.insertar(5)
max_heap.insertar(20)
max_heap.insertar(1)

print(max_heap.extraer_max())  # Salida: 20
print(max_heap.extraer_max())  # Salida: 10
print(max_heap.extraer_max())  # Salida: 5
print(max_heap.extraer_max())  # Salida: 1

# Función para probar Max-Heap
def probar_max_heap():
    heap = MaxHeap()
    inicio = time.time()
    for i in range(10000):
        heap.insertar(i)
    for _ in range(10000):
        heap.extraer_max()
    fin = time.time()
    return fin - inicio

# Función para probar Heap Binomial
def probar_heap_binomial():
    heap = HeapBinomial()
    inicio = time.time()
    for i in range(10000):
        heap.insertar(i)
    for _ in range(10000):
        heap.extraer_min()
    fin = time.time()
    return fin - inicio

# Comparación de tiempos
tiempo_max_heap = probar_max_heap()
tiempo_heap_binomial = probar_heap_binomial()

print(f"Tiempo Max-Heap: {tiempo_max_heap} segundos")
print(f"Tiempo Heap Binomial: {tiempo_heap_binomial} segundos")

