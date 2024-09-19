from random import randint

# Случайный список из 10 элементов от 1 до 99
a = [randint(1, 99) for i in range(10)]


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def comb_sort(arr):
    step, stop = len(arr), False
    while step > 1 or stop:
        step, stop = max(1, int(step / shrink_fact)), False
        for i in range(len(arr) - step):
            if arr[i] > arr[i + step]:
                arr[i], arr[i + step] = arr[i + step], arr[i]
                stop = True
    return arr


shrink_fact = 1.3

print(a, bubble_sort(a), comb_sort(a), sep="\n")
# https://habr.com/ru/articles/204600/
