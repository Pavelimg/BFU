from math import sqrt


def cross_product(a, b, c):  # векторное произведение
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def lines_intersection(A1, B1, C1, A2, B2, C2):  # Пересечение прямых
    denominator = A1 * B2 - A2 * B1
    if denominator == 0:
        return None  # Прямые параллельны
    x = (B1 * C2 - B2 * C1) / denominator
    y = (A2 * C1 - A1 * C2) / denominator
    return (x, y)


def line_segment_intersection(A, B, C, segment):  # Прямая с отрезком
    (x1, y1), (x2, y2) = segment
    A_seg = y2 - y1
    B_seg = x1 - x2
    C_seg = x2 * y1 - x1 * y2
    intersection = lines_intersection(A, B, C, A_seg, B_seg, C_seg)
    if not intersection:
        return None
    x, y = intersection
    # Проверяем, что точка лежит на отрезке
    if (min(x1, x2) <= x <= max(x1, x2)) and (min(y1, y2) <= y <= max(y1, y2)):
        return (x, y)
    return None


def segments_intersect(seg1, seg2):  # Пересечение отрезков
    (x1, y1), (x2, y2) = seg1
    (x3, y3), (x4, y4) = seg2

    d1 = cross_product((x3, y3), (x4, y4), (x1, y1))
    d2 = cross_product((x3, y3), (x4, y4), (x2, y2))
    d3 = cross_product((x1, y1), (x2, y2), (x3, y3))
    d4 = cross_product((x1, y1), (x2, y2), (x4, y4))
    if (d1 * d2 < 0) and (d3 * d4 < 0):
        return True
    # Проверка наложений (если отрезки частично совпадают)
    if d1 == 0 and d2 == 0 and d3 == 0 and d4 == 0:
        if (max(x1, x2) < min(x3, x4)) or (max(x3, x4) < min(x1, x2)):
            return False
        if (max(y1, y2) < min(y3, y4)) or (max(y3, y4) < min(y1, y2)):
            return False
        return True
    return False


def line_circle_intersection(A, B, C, circle):  # прямая и окружность
    xc, yc, R = circle
    distance = abs(A * xc + B * yc + C) / sqrt(A ** 2 + B ** 2)
    if distance > R:
        return []
    # Находим проекцию центра на прямую
    if B == 0:  # Вертикальная прямая
        x_proj = -C / A
        y_proj = yc
    else:
        x_proj = (B * (B * xc - A * yc) - A * C) / (A ** 2 + B ** 2)
        y_proj = (-A * B * xc + A ** 2 * yc - B * C) / (A ** 2 + B ** 2)
    if distance == R:
        return [(x_proj, y_proj)]
    # Две точки пересечения
    d = sqrt(R ** 2 - distance ** 2)
    dx = -B * d / sqrt(A ** 2 + B ** 2)
    dy = A * d / sqrt(A ** 2 + B ** 2)
    return [(x_proj + dx, y_proj + dy), (x_proj - dx, y_proj - dy)]


def segment_circle_intersection(segment, circle):  # Отрезок и окружность
    (x1, y1), (x2, y2) = segment
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2
    intersections = line_circle_intersection(A, B, C, circle)
    result = []
    for (x, y) in intersections:
        if (min(x1, x2) <= x <= max(x1, x2)) and (min(y1, y2) <= y <= max(y1, y2)):
            result.append((x, y))
    return result


def circles_intersection(circle1, circle2):
    x1, y1, R1 = circle1
    x2, y2, R2 = circle2
    d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if d > R1 + R2 or d < abs(R1 - R2):
        return []
    if d == 0 and R1 == R2:
        return []  # Бесконечно много точек (окружности совпадают)
    a = (R1 ** 2 - R2 ** 2 + d ** 2) / (2 * d)
    h = sqrt(R1 ** 2 - a ** 2)
    x0 = x1 + a * (x2 - x1) / d
    y0 = y1 + a * (y2 - y1) / d
    x3 = x0 + h * (y2 - y1) / d
    y3 = y0 - h * (x2 - x1) / d
    x4 = x0 - h * (y2 - y1) / d
    y4 = y0 + h * (x2 - x1) / d
    if x3 == x4 and y3 == y4:
        return [(x3, y3)]
    return [(x3, y3), (x4, y4)]
