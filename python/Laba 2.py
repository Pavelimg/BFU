import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

import numpy as np
import pandas as pd
 # Функция для линейной интерполяции
def linear_interpolate(df):
    """
    Линейная интерполяция для заполнения пропущенных значений в DataFrame.

    Параметры:
    df - DataFrame с колонками 'x' (независимая переменная) и 'y' (зависимая переменная)

    Возвращает:
    DataFrame с заполненными пропусками в колонке 'y' с помощью линейной интерполяции
    """
    # Создаем копию DataFrame чтобы не изменять исходные данные
    df = df.copy()

    # Удаляем строки с пропусками для определения известных точек
    known_points = df.dropna()

    # Если нет известных точек, возвращаем исходный DataFrame
    if len(known_points) < 2:
        raise ValueError("Для линейной интерполяции требуется минимум 2 известные точки")

    # Сортируем точки по x для корректной интерполяции
    known_points = known_points.sort_values('x')
    x_known = known_points['x'].values
    y_known = known_points['y'].values

    # Функция для линейной интерполяции между двумя точками
    def interpolate(x, x0, x1, y0, y1):
        return y0 + (y1 - y0) * (x - x0) / (x1 - x0)

    # Применяем интерполяцию ко всем строкам
    for i in range(len(df)):
        if pd.isna(df.at[i, 'y']):
            x = df.at[i, 'x']

            # Находим ближайшие известные точки
            if x <= x_known[0]:
                # Экстраполяция слева - используем первые две точки
                df.at[i, 'y'] = interpolate(x, x_known[0], x_known[1], y_known[0], y_known[1])
            elif x >= x_known[-1]:
                # Экстраполяция справа - используем последние две точки
                df.at[i, 'y'] = interpolate(x, x_known[-2], x_known[-1], y_known[-2], y_known[-1])
            else:
                # Интерполяция - находим промежуток между известными точками
                for j in range(len(x_known) - 1):
                    if x_known[j] <= x <= x_known[j+1]:
                        df.at[i, 'y'] = interpolate(x, x_known[j], x_known[j+1], y_known[j], y_known[j+1])
                        break

    return df
 # Функция для квадратичной интерполяции
def quadratic_interpolate(df):

    # Создаем копию DataFrame чтобы не изменять исходные данные
    df = df.copy()

    # Удаляем строки с пропусками для определения известных точек
    known_points = df.dropna()

    # Проверяем достаточное количество точек
    if len(known_points) < 3:
        raise ValueError("Для квадратичной интерполяции требуется минимум 3 известные точки")

    # Сортируем точки по x для корректной интерполяции
    known_points = known_points.sort_values('x')
    x_known = known_points['x'].values
    y_known = known_points['y'].values

    # Функция для решения системы уравнений и нахождения коэффициентов параболы
    def quadratic_coefficients(x0, x1, x2, y0, y1, y2):
      # Создаем матрицу коэффициентов системы уравнений для квадратичной функции
        A = np.array([
            [x0**2, x0, 1],
            [x1**2, x1, 1],
            [x2**2, x2, 1]
        ])
        # Создаем вектор правых частей уравнений (значения y)
        b = np.array([y0, y1, y2])
    # Решаем систему линейных уравнений относительно a, b, c
    # Возвращаем коэффициенты квадратичной функции y = a*x² + b*x + c
        return np.linalg.solve(A, b)

    # Применяем интерполяцию ко всем строкам
    for i in range(len(df)):
      # Проверяем, является ли текущее значение y пропущенным (NaN)
        if pd.isna(df.at[i, 'y']):
          # Получаем значение x для текущей строки
            x = df.at[i, 'x']

            # Определяем какие точки использовать для интерполяции
            if x <= x_known[0]:
                # Экстраполяция слева - используем первые три точки
                a, b, c = quadratic_coefficients(x_known[0], x_known[1], x_known[2],
                                                y_known[0], y_known[1], y_known[2])
            elif x >= x_known[-1]:
                # Экстраполяция справа - используем последние три точки
                a, b, c = quadratic_coefficients(x_known[-3], x_known[-2], x_known[-1],
                                                y_known[-3], y_known[-2], y_known[-1])
            else:
                # Интерполяция - находим три ближайшие точки
                for j in range(len(x_known) - 2):
                    if x_known[j] <= x <= x_known[j+2]:
                        a, b, c = quadratic_coefficients(x_known[j], x_known[j+1], x_known[j+2],
                                                         y_known[j], y_known[j+1], y_known[j+2])
                        break

            # Вычисляем значение y по квадратичной формуле
            df.at[i, 'y'] = a * x**2 + b * x + c

    return df

# Загрузка данных, изменяя пустышки на NaN и пропуская первую строку
df = pd.read_excel('Точка росы.xlsx', skiprows=1, na_values=['', 'NA', 'N/A', 'null'])
df = df.iloc[:, 1:]

# Создаем DataFrame
df_optim = pd.DataFrame({
    'x' : [i for i in range(1, 24 * 31 + 1)]
})

# Помещаем столбец из данных excel в один столбец перебирая строки слева на право
df_optim['y'] = pd.DataFrame(df.values.ravel())

# Применяем интерполяции
df_linear = linear_interpolate(df_optim)
df_quadratic = quadratic_interpolate(df_optim)

# Создаем фигуру
plt.figure(figsize=(100, 16))

# Точки (красные кружки)
plt.plot(
    df_linear['x'],
    df_linear['y'],
    marker='o',
    linestyle='',
    markerfacecolor='red',
    markersize=6,
)

# Линейная интерполяция (оранжевая линия)
plt.plot(
    df_linear['x'],
    df_linear['y'],
    color='orange',
    linewidth=2,
    label='Линейная интерполяция'
)

# Настройки графика
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Линейная интерполяция. МЛСП Д_6 Точка росы.   Март 2009', fontsize=14)
plt.xlim(left = 0, right = 744)
plt.legend()
plt.grid()
plt.show()

# Создаем фигуру
plt.figure(figsize=(100, 16))

# Точки (синие кружки)
plt.plot(
    df_quadratic['x'],
    df_quadratic['y'],
    marker='o',
    linestyle='',
    markerfacecolor='blue',
    markersize=6,
)

# Квадратичная интерполяция (зеленая линия)
plt.plot(
    df_quadratic['x'],
    df_quadratic['y'],
    color='green',
    linewidth=2,
    label='Квадратичная интерполяция'
)

# Настройки графика
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Квадратичная интерполяция. МЛСП Д_6 Точка росы.   Март 2009', fontsize=14)
plt.xlim(left = 0, right = 744)
plt.legend()
plt.grid()
plt.show()

# Создаем фигуру
plt.figure(figsize=(100, 16))

# Точки (красные кружки)
plt.plot(
    df_linear['x'],
    df_linear['y'],
    marker='o',
    linestyle='',
    markerfacecolor='red',
    markersize=6,
)

# Точки (синие кружки)
plt.plot(
    df_quadratic['x'],
    df_quadratic['y'],
    marker='o',
    linestyle='',
    markerfacecolor='blue',
    markersize=6,
)

# Линейная интерполяция (оранжевая линия)
plt.plot(
    df_linear['x'],
    df_linear['y'],
    color='orange',
    linewidth=2,
    label='Линейная интерполяция'
)

# Квадратичная интерполяция (зеленая линия)
plt.plot(
    df_quadratic['x'],
    df_quadratic['y'],
    color='green',
    linewidth=2,
    label='Квадратичная интерполяция'
)

# Настройки графика
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Сравнение методов интерполяции. МЛСП Д_6 Точка росы.   Март 2009', fontsize=14)
plt.xlim(left = 0, right = 744)
plt.legend()
plt.grid()
plt.show()

df_result_lin = np.array([f"{df_linear['x'][i]} : {df_linear['y'][i]}" for i in range(len(df_linear['x']))])
df_result_quad = np.array([f"{df_linear['x'][i]} : {df_linear['y'][i]}" for i in range(len(df_quadratic['x']))])

# Записываем результаты
with open('result.txt', 'w') as file:
    file.write("Линейная интерполяция:\n")
    file.write(f"(x час : y °С) : {', '.join(df_result_lin)}\n")

with open('result.txt', 'a') as file:
    file.write("Квадратичная интерполяция:\n")
    file.write(f"(x час : y °С) : {', '.join(df_result_quad)}\n")
