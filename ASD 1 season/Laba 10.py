from random import randint


def merge_sort(A):
    if len(A) == 1 or len(A) == 0:
        return A
    L = merge_sort(A[:len(A) // 2])
    R = merge_sort(A[len(A) // 2:])
    left_counter = right_counter = 0
    sorted_list = []
    while left_counter < len(L) and right_counter < len(R):
        if L[left_counter] <= R[right_counter]:
            sorted_list.append(L[left_counter])
            left_counter += 1
        else:
            sorted_list.append(R[right_counter])
            right_counter += 1

    sorted_list += L[left_counter:]
    sorted_list += R[right_counter:]
    return sorted_list


# Случайный список из 10 элементов от 1 до 99
a = [randint(1, 99) for i in range(10)]
print(a, merge_sort(a.copy()), sep="\n")
