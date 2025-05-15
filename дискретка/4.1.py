import heapq
import math
from string import ascii_lowercase as lowercase
from collections import defaultdict


class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree():
    global frequency
    heap = []
    for char, freq in frequency.items():
        heapq.heappush(heap, HuffmanNode(char=char, freq=freq))

    # Построение дерева Хаффмана
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    return heapq.heappop(heap)


def build_huffman_codes(node, current_code="", codes=None):
    if codes is None:
        codes = {}

    if node.char is not None:
        codes[node.char] = current_code
        return

    build_huffman_codes(node.left, current_code + "0", codes)
    build_huffman_codes(node.right, current_code + "1", codes)

    return codes


def shannon_entropy(frequencies):
    total = sum(frequencies.values())
    entropy = 0.0
    for freq in frequencies.values():
        p = freq / total
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy


def lzw_encode(data, letters):  # LZW
    current, encoded, next_code = "", [], 32
    dictionary = {letters[i]: i for i in range(next_code)}
    for char in data:
        combined = current + char
        if combined in dictionary:
            current = combined
        else:
            encoded.append(dictionary[current])
            dictionary[combined] = next_code
            next_code += 1
            current = char
    if current:
        encoded.append(dictionary[current])

    return encoded


def calculate_encoded_size(encoded_data):  # LZW
    current_bits = 5
    max_code = 31
    total_bits = 0

    for code in encoded_data:
        total_bits += current_bits
        if code > max_code:
            current_bits += 1
            max_code = (1 << current_bits) - 1

    return total_bits


input_text, whitelist = "", ".,! ?'" + lowercase
print(f"Рассматриваем {len(whitelist)} символа: {whitelist}")
with open("War and Peace full.txt") as f:
    for letter in f.read():
        if letter.lower() in whitelist:
            input_text += letter.lower()

frequency = defaultdict(int)
for char in input_text:
    frequency[char] += 1

codes = build_huffman_codes(build_huffman_tree())

print("Частоты и коды Хаффмана:")
for char, code in sorted(codes.items()):
    print(f"'{char}' | {str(frequency[char]).rjust(7, ' ')} | {code} ")
encoded = "".join(list(map(lambda x: codes[x], input_text)))
print(f"Длинна в битах до кодировки по Шенону: {len(input_text) * 5}, после: {len(encoded)}")
print(f"Энтропия Шенона: {shannon_entropy(frequency):.2f}")
print(
    f"Средняя длина кода: {sum(len(code) * frequency[char] for char, code in codes.items()) / len(input_text):.2f} бит на символ")
size_bits = calculate_encoded_size(lzw_encode(input_text, whitelist))
print(f"Размер в битах по LZW: {size_bits}, на {len(encoded) - size_bits} меньше, чем по Шенону")
