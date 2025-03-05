from random import randint


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)


# Случайный список из 10 элементов от 1 до 99
a = [randint(1, 99) for i in range(10)]
print(a, quicksort(a.copy()), sep="\n")
