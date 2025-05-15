import math


def cross_product(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def graham_scan(points):  # Алгоритм Грэхема
    if len(points) < 3:
        return False  # Недостаточно точек для выпуклой оболочки

    start = min(points, key=lambda p: (p[1], p[0]))  # Находим стартовую точку (с минимальной y, затем x)
    sorted_points = sorted(points, key=lambda p: (
        math.atan2(p[1] - start[1], p[0] - start[0]), p))  # Сортируем точки по полярному углу относительно стартовой
    stack = [start, sorted_points[0], sorted_points[1]]

    for i in range(2, len(sorted_points)):
        while len(stack) >= 2 and cross_product(stack[-2], stack[-1], sorted_points[i]) <= 0:
            stack.pop()
        stack.append(sorted_points[i])

    return len(stack) >= 3  # Выпуклая оболочка существует, если в стеке хотя бы 3 точки


print(graham_scan([(0, 0), (2, 0), (1, 2)]))  # True

# Все точки на одной прямой
print(graham_scan([(0, 0), (1, 1), (2, 2), (3, 3)]))  # False

# Квадрат
print(graham_scan([(0, 0), (2, 0), (2, 2), (0, 2)]))  # True

# Всего две точки
print(graham_scan([(0, 0), (1, 1)]))  # False

# Выпуклый пятиугольник
print(graham_scan([(0, 0), (2, 0), (3, 1), (2, 2), (0, 2)]))  # True

# Одна точка внутри выпуклой оболочки
print(graham_scan([(0, 0), (3, 0), (3, 3), (0, 3), (1, 1)]))  # True

# Точки образуют "звезду" (невыпуклый многоугольник)
print(graham_scan([(0, 0), (2, 2), (4, 0), (2, 1)]))  # True (но оболочка будет выпуклой)

# Точки на окружности (все в выпуклой оболочке)
print(graham_scan([(0, 0), (1, 1), (0, 2), (-1, 1)]))  # True

# Некоторые точки совпадают
print(graham_scan([(0, 0), (1, 1), (1, 1), (2, 2)]))  # False (коллинеарны)

print(graham_scan([(0, 0), (4, 0), (4, 4), (2, 2), (0, 4)]))  # True
