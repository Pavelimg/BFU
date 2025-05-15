import sympy as sp  # Импорт библиотеки для символьных вычислений
import numpy as np  # Импорт библиотеки для численных операций
import matplotlib.pyplot as plt  # Импорт библиотеки для визуализации

# Определение символьной переменной и сложной математической функции
x = sp.symbols('x')
f = sp.exp(-x ** 2) * sp.sin(3 * x)  # Комбинация экспоненты и синуса

# Пределы интегрирования
a, b = 0, 2

# Попытка аналитического вычисления интеграла
analytic_integral = sp.integrate(f, (x, a, b))

# Проверка, удалось ли вычислить интеграл аналитически
if isinstance(analytic_integral, sp.Integral):
    exact = sp.N(analytic_integral)  # Численное вычисление, если не получилось аналитически
else:
    exact = float(analytic_integral)  # Преобразование аналитического результата в float

print(f"Точное значение интеграла: {exact:.8f}")  # Вывод точного значения


# Реализация метода трапеций для численного интегрирования
def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n  # Шаг интегрирования
    x_vals = np.linspace(a, b, n + 1)  # Равномерная сетка
    y_vals = f(x_vals)  # Значения функции на сетке
    return h * (0.5 * y_vals[0] + 0.5 * y_vals[-1] + np.sum(y_vals[1:-1]))  # Формула трапеций


# Реализация метода Симпсона для численного интегрирования
def simpson_rule(f, a, b, n):
    if n % 2 != 0:
        n += 1  # Корректировка для четного количества интервалов
    h = (b - a) / n
    x_vals = np.linspace(a, b, n + 1)
    y_vals = f(x_vals)
    return (h / 3) * (
                y_vals[0] + y_vals[-1] + 4 * np.sum(y_vals[1:-1:2]) + 2 * np.sum(y_vals[2:-2:2]))  # Формула Симпсона


# Параметры численного интегрирования
n = 100
f_np = lambda x: np.exp(-x ** 2) * np.sin(3 * x)  # Адаптация функции для numpy

# Вычисление интегралов численными методами
trap_result = trapezoidal_rule(f_np, a, b, n)
simp_result = simpson_rule(f_np, a, b, n)

# Расчет ошибок методов
trap_error = abs(trap_result - exact)
simp_error = abs(simp_result - exact)

# Вывод результатов сравнения
print(f"Метод трапеций: {trap_result:.8f}, ошибка: {trap_error:.2e}")
print(f"Метод Симпсона: {simp_result:.8f}, ошибка: {simp_error:.2e}")

# Исследование зависимости ошибки от количества разбиений
ns = np.array([10, 50, 100, 500, 1000])  # Различные количества разбиений
trap_errors = []  # Ошибки метода трапеций
simp_errors = []  # Ошибки метода Симпсона

# Вычисление ошибок для разных n
for n_current in ns:
    trap_errors.append(abs(trapezoidal_rule(f_np, a, b, n_current) - exact))
    simp_errors.append(abs(simpson_rule(f_np, a, b, n_current) - exact))

# Построение графика сравнения ошибок
plt.figure(figsize=(10, 5))
plt.plot(ns, trap_errors, 'o-', label='Метод трапеций')  # График ошибок трапеций
plt.plot(ns, simp_errors, 's-', label='Метод Симпсона')  # График ошибок Симпсона
plt.xlabel('Число разбиений (n)')  # Подпись оси X
plt.ylabel('Абсолютная ошибка')  # Подпись оси Y
plt.yscale('log')  # Логарифмическая шкала для Y
plt.legend()  # Отображение легенды
plt.grid()  # Включение сетки
plt.show()  # Показ графика
