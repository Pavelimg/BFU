def hash_function(string, table_size):
    return sum(ord(char) for char in string) % table_size
    # хеш-функция, основанная на сумме ASCII-кодов символов


def create_hash_table(file_path, table_size):
    # Создаем пустую хеш-таблицу
    hash_table = [[] for _ in range(table_size)]

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  # Убираем лишние пробелы и переносы строк

            if not line:  # Пропускаем пустые строки
                continue

            # Рассчитываем индекс для данной строки
            index = hash_function(line, table_size)

            # Добавляем строку в соответствующий список
            hash_table[index].append(line)

    return hash_table


file_path, table_size = 'input.txt', 10
table = create_hash_table(file_path, table_size)

for i, element in enumerate(table):
    print(f"Элемент {i}: {element}")
