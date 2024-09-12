from random import randint

# Случайный список из 10 элементов от 1 до 99
a = [randint(1, 99) for i in range(10)]


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(a, bubble_sort(a), sep="\n")
# https://habr.com/ru/articles/204600/
