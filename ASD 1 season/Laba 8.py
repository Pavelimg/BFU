from random import randint

# Случайный список из 10 элементов от 1 до 99
a = [randint(1, 99) for i in range(10)]

length = len(str(max(a)))
rang = 10


def radix_sort(arr):
    for i in range(length):  # повторяем для каждого разряда чисел
        sublist = [[] for _ in range(rang)]  # создаём 10 пустых списков (для каждой цифры)
        [sublist[x // 10 ** i % 10].append(x) for x in arr]  # в соответствующие списки добавляем элементы
        arr = []
        # например, для первой итерации чисел [21, 123, 666] получим [[],[21],[],[123],[],[],[666],[],[],[]]
        for j in range(rang):
            arr += sublist[j]
    return arr


print(a, radix_sort(a), sep="\n")
# https://foxford.ru/wiki/informatika/porazryadnaya-sortirovka
