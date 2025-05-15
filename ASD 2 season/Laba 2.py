from itertools import combinations
from elements_interaction_for_laba_2 import *


def area(a, b, c):
    return abs((a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2)


def is_point_inside_triangle(p, triangle):
    a, b, c = triangle
    total_area = area(a, b, c)
    if total_area < 1e-9:  # Вырожденный треугольник (точки на одной прямой)
        return False
    sum_areas = area(p, b, c) + area(a, p, c) + area(a, b, p)
    return abs(total_area - sum_areas) < 1e-9


def has_nested_triangles(points):
    if len(points) < 6:
        return False

    triangles = [t for t in combinations(points, 3) if area(*t) > 1e-9]  # Только невырожденные
    for i in range(len(triangles)):
        for j in range(i + 1, len(triangles)):
            t1, t2 = triangles[i], triangles[j]
            # Проверяем, что все вершины t1 внутри t2 и нет пересечений сторон
            if (all(is_point_inside_triangle(p, t2) for p in t1) and
                    not any(segments_intersect(seg1, seg2)
                            for seg1 in combinations(t1, 2)
                            for seg2 in combinations(t2, 2))):
                return True
            # Проверяем, что все вершины t2 внутри t1 и нет пересечений сторон
            if (all(is_point_inside_triangle(p, t1) for p in t2) and
                    not any(segments_intersect(seg1, seg2)
                            for seg1 in combinations(t1, 2)
                            for seg2 in combinations(t2, 2))):
                return True
    return False


# Два явно вложенных треугольника (один внутри другого)
print(has_nested_triangles([(0, 0), (4, 0), (2, 4), (1, 1), (3, 1), (2, 2)]))  # True

# Все точки коллинеарны (нет треугольников)
print(has_nested_triangles([(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]))  # False

# Три треугольника, один внутри другого
print(has_nested_triangles([(0, 0), (6, 0), (3, 6), (2, 1), (4, 1), (3, 2), (3, 1.5)]))  # True

# Два пересекающихся треугольника (не вложены)
print(has_nested_triangles([(0, 0), (4, 0), (2, 4), (1, -1), (3, -1), (2, 5)]))  # False

# Множество точек, образующих несколько треугольников, но без вложенности
print(has_nested_triangles([(0, 0), (2, 0), (1, 2), (3, 0), (5, 0), (4, 2)]))  # False

# Точки образуют "звезду" с вложенным треугольником
print(has_nested_triangles([(0, 0), (4, 0), (2, 4), (2, 0), (3, 2), (1, 2)]))  # True

# Все точки кроме одной лежат на окружности
print(has_nested_triangles([(0, 0), (2, 2), (0, 4), (-2, 2), (1, 2)]))  # False

# Два отдельных треугольника
print(has_nested_triangles([(0, 0), (2, 0), (1, 2), (10, 0), (12, 0), (11, 2)]))  # False

# Треугольник с точкой точно в центре
print(has_nested_triangles([(0, 0), (4, 0), (2, 4), (2, 1.333)]))  # False

print(has_nested_triangles([(0, 0), (8, 0), (4, 8), (2, 0), (6, 0), (4, 4), (3, 2), (5, 2), (4, 3)]))  # True
