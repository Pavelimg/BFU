from random import randint

# Случайный список из 10 элементов от 1 до 99
a = [randint(1, 99) for i in range(4)]
print(a)


def selection_sort_simple_1(arr):
    for i in range(len(arr) - 1, 0, -1):
        max_element_index = arr.index(max(arr[:i + 1]))
        arr[i], arr[max_element_index] = arr[max_element_index], arr[i]
        return arr


def selection_sort_simple_2(arr):
    for i in range(len(arr) - 1, 0, -1):
        max_element_index = -1
        max_element = 0
        for index, element in enumerate(arr):
            if element >= max_element:
                max_element = element
                max_element_index = index
        arr[i], arr[max_element_index] = arr[max_element_index], arr[i]
    return arr


def selection_sort_double(arr):
    pass


print(selection_sort_simple_1(a), selection_sort_simple_2(a), selection_sort_double(a), sep="\n")
# https://habr.com/ru/articles/422085/
