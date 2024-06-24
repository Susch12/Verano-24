import time
import random
import matplotlib.pyplot as plt
from skew_heap import SkewHeap  # Asegúrate de tener esta implementación
from binary_heap import BinaryHeap  # Asegúrate de tener esta implementación

# Función para medir el tiempo de una operación
def measure_time(heap, operation, *args):
    start = time.time()
    result = getattr(heap, operation)(*args)
    end = time.time()
    return end - start

# Generar datos de prueba
def generate_data(size):
    return [random.randint(0, 100000) for _ in range(size)]

# Comparar tiempos de ejecución
def compare_heaps(skew_heap, binary_heap, data):
    skew_heap_insert_times = []
    binary_heap_insert_times = []
    skew_heap_delete_min_times = []
    binary_heap_delete_min_times = []

    # Medir tiempos de inserción
    for x in data:
        skew_heap_insert_times.append(measure_time(skew_heap, 'insert', x))
        binary_heap_insert_times.append(measure_time(binary_heap, 'insert', x))

    # Medir tiempos de eliminación del mínimo
    for _ in range(len(data)):
        skew_heap_delete_min_times.append(measure_time(skew_heap, 'delete_min'))
        binary_heap_delete_min_times.append(measure_time(binary_heap, 'delete_min'))

    # Calcular promedios
    avg_skew_insert = sum(skew_heap_insert_times) / len(skew_heap_insert_times)
    avg_binary_insert = sum(binary_heap_insert_times) / len(binary_heap_insert_times)
    avg_skew_delete_min = sum(skew_heap_delete_min_times) / len(skew_heap_delete_min_times)
    avg_binary_delete_min = sum(binary_heap_delete_min_times) / len(binary_heap_delete_min_times)

    return {
        'avg_skew_insert': avg_skew_insert,
        'avg_binary_insert': avg_binary_insert,
        'avg_skew_delete_min': avg_skew_delete_min,
        'avg_binary_delete_min': avg_binary_delete_min
    }

# Main
if __name__ == "__main__":
    data_size = 1000  # Tamaño de los datos de prueba
    iterations = 100  # Número de iteraciones

    skew_insert_times = []
    binary_insert_times = []
    skew_delete_min_times = []
    binary_delete_min_times = []

    for _ in range(iterations):
        data = generate_data(data_size)
        skew_heap = SkewHeap()
        binary_heap = BinaryHeap()
        results = compare_heaps(skew_heap, binary_heap, data)

        skew_insert_times.append(results['avg_skew_insert'])
        binary_insert_times.append(results['avg_binary_insert'])
        skew_delete_min_times.append(results['avg_skew_delete_min'])
        binary_delete_min_times.append(results['avg_binary_delete_min'])

    # Graficar resultados
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(range(iterations), skew_insert_times, label='Skew Heap Insertar')
    plt.plot(range(iterations), binary_insert_times, label='Binary Heap Insertar')
    plt.xlabel('Ejecución ')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparación de la función Insertar')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(range(iterations), skew_delete_min_times, label='Skew Heap Borrar el minimo')
    plt.plot(range(iterations), binary_delete_min_times, label='Binary Heap Borrar el minimo')
    plt.xlabel('Ejecución')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparacion de la función Eliminar')
    plt.legend()

    plt.tight_layout()
    plt.show()
