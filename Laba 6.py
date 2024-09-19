from random import randint

# Случайный список из 10 элементов от 1 до 99
a = [randint(1, 99) for i in range(10)]


def selection_sort_simple_1(arr):
    for i in range(len(arr) - 1, 0, -1):
        max_element_index = arr.index(max(arr[:i + 1]))
        arr[i], arr[max_element_index] = arr[max_element_index], arr[i]
    return arr


def selection_sort_simple_2(arr):
    i = 0
    while i < len(arr) - 1:
        m = i
        j = i + 1
        while j < len(arr):
            if arr[j] < arr[m]:
                m = j
            j += 1
        arr[i], arr[m] = arr[m], arr[i]
        i += 1
    return arr


print(a, selection_sort_simple_1(a.copy()), selection_sort_simple_2(a.copy()), sep="\n")

# https://habr.com/ru/articles/422085/
# https://younglinux.info/algorithm/sort_min
