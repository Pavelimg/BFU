from random import randint

# Случайный список из 10 элементов от 1 до 99
a = [randint(1, 99) for i in range(10)]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:  # j > 0 что-бы при встрече наименьшего элемента не было IndexOutOfRange
            arr[j - 1], arr[j] = arr[j], arr[
                j - 1]  # Пока a[j] элемент не встанет на своё место, меняем его с соседом слева
            j -= 1
    return arr


print(a, insertion_sort(a), sep="\n")
# https://habr.com/ru/articles/181271/
