def hash_function(string):
    return sum(ord(char) for char in string) % move
    # хеш-функция, основанная на сумме ASCII-кодов символов


def create_hash_table(file_path, table_size):
    # Создаем пустую хеш-таблицу
    hash_table = [None for _ in range(table_size)]

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  # Убираем лишние пробелы и переносы строк

            if not line:  # Пропускаем пустые строки
                continue

            # Рассчитываем индекс для данной строки
            index = hash_function(line)

            collisions = 0
            while hash_table[collisions * move + index]:  # Ищем ближайшее свободное место
                collisions += 1

            # Добавляем строку
            hash_table[collisions * move + index] = line

    return hash_table


move = 10  # сдивг для Хэш-функции (Что бы продемонстрировать коллизии. Например "a" и "k")
table = create_hash_table('../input.txt', 1000)

for i, element in enumerate(table):
    if element:
        print(f"Элемент {i}: {element}")
