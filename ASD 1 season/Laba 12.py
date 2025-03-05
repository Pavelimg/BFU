import heapq
import random

# Генерим случайный файл
input_path = "../input.txt"
with open(input_path, 'w') as example:
    for x in range(1000):
        example.writelines(str(random.randint(0, 100000)) + '\n')


def create_sorted_chunks(input_path, chunk_size):
    chunks = []
    with open(input_path, 'r') as file:
        chunk = []
        for line in file:
            chunk.append(int(line.strip()))
            if len(chunk) == chunk_size:
                chunk.sort()
                chunks.append(chunk)
                chunk = []

        if chunk:
            chunk.sort()
            chunks.append(chunk)

    return chunks


def merge_sorted_chunks(chunks, output_path):
    # Работаем с кучей
    heap = [(chunk[0], i, 0) for i, chunk in enumerate(chunks) if chunk]
    heapq.heapify(heap)

    with open(output_path, 'w') as file:
        while heap:
            value, chunk_index, element_index = heapq.heappop(heap)
            file.write(str(value) + '\n')

            if element_index + 1 < len(chunks[chunk_index]):
                next_element = chunks[chunk_index][element_index + 1]
                heapq.heappush(heap, (next_element, chunk_index, element_index + 1))


output_path = "../output.txt"
chunk_size = 100

merge_sorted_chunks(create_sorted_chunks(input_path, chunk_size), output_path)
