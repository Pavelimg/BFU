import numpy as np
import matplotlib.pyplot as plt
import gsw
import pandas as pd

def clear_file(file_path):
    with open(file_path, 'w') as file:
        file.write('')
    return file_path

def calculate_gradient(z, S, method="left"):
    """Вычисляет вертикальный градиент солености методом левого разностного приближения."""
    gradient = np.zeros_like(S, dtype=float)  # Создаем массив для градиентов

    # Обратное (левое) разностное приближение
    for i in range(1, len(S)):
        gradient[i] = (S[i] - S[i-1]) / (z[i] - z[i-1])  # Расчет градиента как разность текущего и предыдущего значений

    # Первому элементу присваиваем значение второго, так как для первого элемента нет предыдущего
    gradient[0] = gradient[1] if len(S) > 1 else 0

    return gradient

def halocline(depth, salinity_gradient):
    """Находит галоклин и выводит на какой глубине"""
    max_gradient_index = np.argmax(np.abs(salinity_gradient)) #индекс максимального градиента
    halocline_depth = depth[max_gradient_index]  # Используем max_gradient_index
    return f"Галоклин находится на глубине {halocline_depth:.2f} м с градиентом {salinity_gradient[max_gradient_index]} PSU/м."

file_path = '/Фрагмент массива данных CTD-зондирования.xlsx'
df = pd.read_excel(file_path)
Station, Latitude, Longitude, Date, Pressure, Depth, Temperature, Conductivity = df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], df.iloc[:, 6], df.iloc[:, 8], df.iloc[:, 9]
check, n, m = Date[1], 0, 1

# Открываем файл для записи результатов
with open('/result.txt', 'a') as file:
    for i in range(1, len(Date)):
        if check != Date[i]:
            check = Date[i]
            n = i
            z = np.array([float(Depth[j]) for j in range(m, n) if float(Depth[j]) >= 15])
            C = np.array([float(Conductivity[j]) for j in range(m, n) if float(Depth[j]) >= 15])
            T = np.array([float(Temperature[j]) for j in range(m, n) if float(Depth[j]) >= 15])
            P = np.array([float(Pressure[j]) for j in range(m, n) if float(Depth[j]) >= 15])
            m = n
            sort_idx = np.argsort(z)
            z_s = z[sort_idx]
            T_s  = T[sort_idx]
            P_s  = P[sort_idx]
            C_s  = C[sort_idx]
            k = len(C)

            # Пример данных: глубина [м] и соленость [PSU]
            S = np.array([gsw.SP_from_C(C_s[j], T_s[j], P_s[j]) for j in range(k)])
            SA = np.array([gsw.SA_from_SP(S[j], P_s[j], Longitude[i - 1], Latitude[i - 1]) for j in range(k)])

            # Расчет градиента
            gradient = calculate_gradient(z_s, S, method='left')
            gradient1 = calculate_gradient(z_s, SA, method='left')  # Используем z_s для SA

            # Профиль солености
            plt.figure(figsize=(20, 16))
            plt.plot(S, z_s, 'o-')
            plt.ylim(bottom=14.9)
            plt.gca().invert_yaxis()
            plt.title(f"Соленость, Дата: {Date[i - 1]}, Станиция: {Station[i - 1]}")
            plt.xlabel('Соленость (PSU)')
            plt.ylabel('Глубина (м)')
            plt.grid()
            plt.show()

            # График градиента
            plt.figure(figsize=(20, 16))
            plt.plot(gradient, z_s, 's--')
            plt.ylim(bottom=14.9)
            plt.gca().invert_yaxis()
            plt.title(f"Вертикальный градиент солености, Дата: {Date[i - 1]}, Станиция: {Station[i - 1]}")
            plt.xlabel('Градиент (PSU/м)')
            plt.grid()
            plt.show()

            # Профиль абсолютной солености
            plt.figure(figsize=(20, 16))
            plt.plot(SA, z_s, 'o-')
            plt.ylim(bottom=14.9)
            plt.gca().invert_yaxis()
            plt.title(f"Абсолютная соленость, Дата: {Date[i - 1]}, Станиция: {Station[i - 1]}")
            plt.xlabel('Соленость (PSU)')
            plt.ylabel('Глубина (м)')
            plt.grid()
            plt.show()

            # График градиента
            plt.figure(figsize=(20, 16))
            plt.plot(gradient1, z_s, 's--')
            plt.ylim(bottom=14.9)
            plt.gca().invert_yaxis()
            plt.title(f"Вертикальный градиент абсолютной солености, Дата: {Date[i - 1]}, Станиция: {Station[i - 1]}")
            plt.xlabel('Градиент (PSU/м)')
            plt.grid()
            plt.show()

            # Запись результатов в файл
            file.write(f'Дата: {Date[i - 1]}, Станиция: {Station[i - 1]}\n')
            file.write(halocline(z_s, gradient) + '\n')
            file.write(f"Соленость: {' '.join(str(x) for x in S)}\n")
            file.write(f"Вертикальный градиент солености: {' '.join(str(x) for x in gradient)}\n")
            file.write(f"Абсолютная соленость: {' '.join(str(x) for x in SA)}.\n")
            file.write(f"Вертикальный градиент абсолютной солености: {' '.join(str(x) for x in gradient1)}\n\n")
