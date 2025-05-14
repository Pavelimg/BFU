import matplotlib.pyplot as plt  # Для построения графиков
import pandas as pd  # Для работы с табличными данными
import numpy as np  # Для числовых операций
from scipy.interpolate import interp1d  # Для интерполяции

plt.style.use('_mpl-gallery')  # Стиль графиков

# Загрузка данных из CSV файла (разделитель - точка с запятой)
file_path = 'data2.csv'
data = pd.read_csv(file_path, sep=";", header=None)  # Читаем без заголовков

# Транспонируем данные - теперь строки = часы (0-23), столбцы = дни (1-31)
data = data.T  # Преобразуем структуру данных

# Настройки параметров
hours = 24  # Количество часов в сутках (0-23)
days = 31  # Количество дней в месяце (1-31)

# Создаем пустую матрицу для температур (часы × дни)
temperature_grid = np.empty((hours, days))  # Инициализация массива
temperature_grid[:] = np.nan  # Заполняем значениями NaN (не числа)

# Заполняем матрицу известными значениями из данных
for hour in range(hours):  # Перебираем все часы
    for day in range(days):  # Перебираем все дни
        if day < len(data.columns):  # Проверяем, есть ли данные для этого дня
            val = data.iloc[hour, day]  # Получаем значение температуры
            if not pd.isna(val) and val != '':  # Если значение не пустое
                try:
                    temperature_grid[hour, day] = float(val)  # Записываем в матрицу
                except:
                    continue  # Пропускаем ошибки преобразования


# Функция для интерполяции пропущенных значений
def interpolate_missing(data):
    linear_filled = np.copy(data)  # Копия для линейной интерполяции
    quadratic_filled = np.copy(data)  # Копия для квадратичной интерполяции

    for hour in range(hours):  # Для каждого часа
        # Находим дни с известными значениями для этого часа
        known_days = np.where(~np.isnan(data[hour]))[0]  # Индексы дней с данными
        known_values = data[hour, known_days]  # Соответствующие температуры

        if len(known_days) >= 2:  # Если есть хотя бы 2 точки
            # Линейная интерполяция
            f_linear = interp1d(known_days, known_values, kind='linear',
                                bounds_error=False, fill_value=np.nan)  # Создаем функцию интерполяции
            linear_filled[hour] = f_linear(np.arange(days))  # Применяем ко всем дням

            if len(known_days) >= 3:  # Если есть хотя бы 3 точки
                # Квадратичная интерполяция
                coeffs = np.polyfit(known_days, known_values, 2)  # Находим коэффициенты параболы
                quadratic_filled[hour] = np.polyval(coeffs, np.arange(days))  # Вычисляем значения

    return linear_filled, quadratic_filled  # Возвращаем результаты


# Выполняем интерполяцию для всей сетки
linear_grid, quadratic_grid = interpolate_missing(temperature_grid)

# Подготовка данных для визуализации
original_points = {'day': [], 'hour': [], 'temp': []}  # Исходные данные
linear_points = {'day': [], 'hour': [], 'temp': []}  # Линейная интерполяция
quadratic_points = {'day': [], 'hour': [], 'temp': []}  # Квадратичная интерполяция

for hour in range(hours):  # Перебираем часы
    for day in range(days):  # Перебираем дни
        temp = temperature_grid[hour, day]  # Исходное значение
        if not np.isnan(temp):  # Если значение есть
            original_points['day'].append(day + 1)  # Сохраняем день (1-31)
            original_points['hour'].append(hour)  # Сохраняем час (0-23)
            original_points['temp'].append(temp)  # Сохраняем температуру
        else:  # Если значение отсутствует
            # Проверяем интерполированные значения
            if not np.isnan(linear_grid[hour, day]):  # Если есть линейная интерполяция
                linear_points['day'].append(day + 1)
                linear_points['hour'].append(hour)
                linear_points['temp'].append(linear_grid[hour, day])

            if not np.isnan(quadratic_grid[hour, day]):  # Если есть квадратичная интерполяция
                quadratic_points['day'].append(day + 1)
                quadratic_points['hour'].append(hour)
                quadratic_points['temp'].append(quadratic_grid[hour, day])

# Создаем 3D график
fig = plt.figure(figsize=(16, 10))  # Размер графика
ax = fig.add_subplot(111, projection='3d')  # 3D проекция

# Отображаем исходные данные (синие точки)
ax.scatter(original_points['day'], original_points['hour'], original_points['temp'],
           c='blue', label='Исходные данные', alpha=0.9, s=30)

# Отображаем линейную интерполяцию (зеленые точки)
if linear_points['day']:  # Если есть что отображать
    ax.scatter(linear_points['day'], linear_points['hour'], linear_points['temp'],
               c='green', label='Линейная интерполяция', alpha=0.7, s=20)

# Отображаем квадратичную интерполяцию (красные точки)
if quadratic_points['day']:  # Если есть что отображать
    ax.scatter(quadratic_points['day'], quadratic_points['hour'], quadratic_points['temp'],
               c='red', label='Квадратичная интерполяция', alpha=0.7, s=20)

# Настройки внешнего вида графика
ax.set_xlabel('День месяца', fontsize=12)  # Подпись оси X
ax.set_ylabel('Час дня', fontsize=12)  # Подпись оси Y
ax.set_zlabel('Температура (°C)', fontsize=12)  # Подпись оси Z
ax.set_title('Температура по дням и часам с интерполяцией пропущенных значений', fontsize=14)
ax.set_xlim(1, 31)  # Границы оси X (дни)
ax.set_ylim(0, 23)  # Границы оси Y (часы)
# Границы оси Z (температура) с небольшим запасом
ax.set_zlim(np.nanmin(temperature_grid) - 2, np.nanmax(temperature_grid) + 2)
ax.set_xticks(np.arange(1, 32, 2))  # Метки на оси X (каждый второй день)
ax.set_yticks(np.arange(0, 24, 3))  # Метки на оси Y (каждые 3 часа)
ax.legend(fontsize=10)  # Легенда графика

plt.tight_layout()  # Оптимизация расположения элементов
plt.show()  # Показать график
