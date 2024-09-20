from random import randint

# Случайный список из 10 элементов от 1 до 99
array = [randint(1, 99) for i in range(4)]


def shell_sort(arr):
    step, last_index = len(arr) // 2, len(arr)
    while step > 0:
        for i in range(step, last_index):
            a = i
            b = a - step
            while b >= 0 and arr[b] > arr[a]:
                arr[b], arr[a] = arr[a], arr[b]
                a = b
                b = a - step
        step //= 2  # Или любое другое значение (см. ссылки)
    return arr


print(array, shell_sort(array.copy()), sep="\n")
# https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D0%A8%D0%B5%D0%BB%D0%BB%D0%B0#%D0%92%D1%8B%D0%B1%D0%BE%D1%80_%D0%B4%D0%BB%D0%B8%D0%BD%D1%8B_%D0%BF%D1%80%D0%BE%D0%BC%D0%B5%D0%B6%D1%83%D1%82%D0%BA%D0%BE%D0%B2
