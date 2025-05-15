# Импорт необходимых библиотек
import numpy as np  # Для работы с массивами данных и математическими операциями
import matplotlib.pyplot as plt  # Для построения графиков
from scipy.optimize import curve_fit  # Для аппроксимации данных методом наименьших квадратов

# Загрузка данных из текстового файла
# Файл должен содержать две колонки чисел, разделенных запятыми (например: "1,59")
data = np.loadtxt('Laba 4.txt', delimiter=',')  # Чтение файла с разделителем-запятой
x_data = data[:, 0]  # Первая колонка - значения по оси X
y_data = data[:, 1]  # Вторая колонка - значения по оси Y


# Определение функций для различных типов аппроксимации:

# 1. Линейная функция (y = ax + b)
def linear(x, a, b):
    return a * x + b


# 2. Квадратичная функция (y = ax² + bx + c)
def quadratic(x, a, b, c):
    return a * x ** 2 + b * x + c


# 3. Кубическая функция (y = ax³ + bx² + cx + d)
def cubic(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d


# 4. Степенная функция (y = ax^b)
def power_law(x, a, b):
    return a * x ** b


# 5. Показательная функция (y = ae^(bx))
def exponential(x, a, b):
    return a * np.exp(b * x)


# 6. Дробно-линейная функция (y = a/(x + b))
def rational(x, a, b):
    return a / (x + b)


# 7. Логарифмическая функция (y = a·ln(x) + b)
def logarithmic(x, a, b):
    return a * np.log(x) + b


# 8. Гиперболическая функция (y = a/x + b)
def hyperbolic(x, a, b):
    return a / x + b


# Подгонка параметров для каждой модели:

# Для сложных функций увеличиваем maxfev (максимальное число вызовов функции) до 5000
# и задаем начальные приближения p0, чтобы помочь алгоритму сходиться

try:
    # 1. Линейная аппроксимация
    popt_linear = curve_fit(linear, x_data, y_data)[0]

    # 2. Квадратичная аппроксимация
    popt_quadratic = curve_fit(quadratic, x_data, y_data)[0]

    # 3. Кубическая аппроксимация
    popt_cubic = curve_fit(cubic, x_data, y_data)[0]

    # 4. Степенная аппроксимация (начальные значения a=1, b=1)
    popt_power = curve_fit(power_law, x_data, y_data, p0=[1, 1], maxfev=5000)[0]

    # 5. Показательная аппроксимация (начальные значения a=1, b=0.1)
    popt_exp = curve_fit(exponential, x_data, y_data, p0=[1, 0.1], maxfev=5000)[0]

    # 6. Дробно-линейная аппроксимация
    popt_rational = curve_fit(rational, x_data, y_data, maxfev=5000)[0]

    # 7. Логарифмическая аппроксимация
    popt_log = curve_fit(logarithmic, x_data, y_data)[0]

    # 8. Гиперболическая аппроксимация
    popt_hyper = curve_fit(hyperbolic, x_data, y_data)[0]

except Exception as e:
    # Вывод сообщения об ошибке, если какая-то аппроксимация не удалась
    print(f"Ошибка при подгонке моделей: {e}")

# Создание сетки графиков
plt.figure(figsize=(20, 16))
x_fit = np.linspace(min(x_data), max(x_data), 500)

# 1. Линейная регрессия
plt.subplot(4, 2, 1)
plt.scatter(x_data, y_data, label='Данные')
plt.plot(x_fit, linear(x_fit, *popt_linear), 'r-', label=f'Линейная: {popt_linear[0]:.2f}x + {popt_linear[1]:.2f}')
plt.title('Линейная регрессия')
plt.legend()

# 2. Квадратичная регрессия
plt.subplot(4, 2, 2)
plt.scatter(x_data, y_data, label='Данные')
plt.plot(x_fit, quadratic(x_fit, *popt_quadratic), 'r-',
         label=f'Квадратичная: {popt_quadratic[0]:.2f}x² + {popt_quadratic[1]:.2f}x + {popt_quadratic[2]:.2f}')
plt.title('Квадратичная регрессия')
plt.legend()

# 3. Кубическая регрессия
plt.subplot(4, 2, 3)
plt.scatter(x_data, y_data, label='Данные')
plt.plot(x_fit, cubic(x_fit, *popt_cubic), 'r-',
         label=f'Кубическая: {popt_cubic[0]:.2f}x³ + {popt_cubic[1]:.2f}x² + {popt_cubic[2]:.2f}x + {popt_cubic[3]:.2f}')
plt.title('Кубическая регрессия')
plt.legend()

# 4. Степенная функция
plt.subplot(4, 2, 4)
plt.scatter(x_data, y_data, label='Данные')
plt.plot(x_fit, power_law(x_fit, *popt_power), 'r-',
         label=f'Степенная: {popt_power[0]:.2f}x^{popt_power[1]:.2f}')
plt.title('Степенная регрессия')
plt.legend()

# 5. Показательная функция
plt.subplot(4, 2, 5)
plt.scatter(x_data, y_data, label='Данные')
plt.plot(x_fit, exponential(x_fit, *popt_exp), 'r-',
         label=f'Показательная: {popt_exp[0]:.2f}e^{popt_exp[1]:.2f}x')
plt.title('Показательная регрессия')
plt.legend()

# 6. Дробно-линейная функция
plt.subplot(4, 2, 6)
plt.scatter(x_data, y_data, label='Данные')
plt.plot(x_fit, rational(x_fit, *popt_rational), 'r-',
         label=f'Дробно-линейная: {popt_rational[0]:.2f}/(x + {popt_rational[1]:.2f})')
plt.title('Дробно-линейная регрессия')
plt.legend()

# 7. Логарифмическая функция
plt.subplot(4, 2, 7)
plt.scatter(x_data, y_data, label='Данные')
plt.plot(x_fit, logarithmic(x_fit, *popt_log), 'r-',
         label=f'Логарифмическая: {popt_log[0]:.2f}ln(x) + {popt_log[1]:.2f}')
plt.title('Логарифмическая регрессия')
plt.legend()

# 8. Гиперболическая зависимость
plt.subplot(4, 2, 8)
plt.scatter(x_data, y_data, label='Данные')
plt.plot(x_fit, hyperbolic(x_fit, *popt_hyper), 'r-',
         label=f'Гиперболическая: {popt_hyper[0]:.2f}/x + {popt_hyper[1]:.2f}')
plt.title('Гиперболическая регрессия')
plt.legend()

plt.tight_layout()
plt.show()
