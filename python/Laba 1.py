import pandas
import gsw

import matplotlib.pyplot as plt


# forward
def vertical_salinity_gradient(salinity, depth):
    dz = depth[1] - depth[0]
    gradient = []

    # Центральная разность для внутренних точек
    for i in range(1, len(depth) - 1):
        grad = (salinity[i + 1] - salinity[i - 1]) / (2 * dz)
        gradient.append(grad)

    front_diff = (salinity[1] - salinity[0]) / dz
    back_diff = (salinity[-1] - salinity[-2]) / dz

    gradient.insert(0, front_diff)
    gradient.append(back_diff)

    return gradient


file_path = 'data1.csv'
input_data = pandas.read_csv(file_path)

filter_data = input_data[input_data['Depth [m]'] >= 15]  # Фильтруем значение с глубины менее 15 метров

# получаем Солёность (aka Sal) из проводимости, температуры, давления
filter_data["SP"] = gsw.SP_from_C(filter_data["Conductivity [mS/cm]"], filter_data["Temperature [degrees_C]"],
                                  filter_data["Pressure"])

# Получаем Абсолютную солёность (aka SA) из обычной солёности и широты с долготой
filter_data["SA"] = gsw.SA_from_SP_Baltic(filter_data["SP"], filter_data["Longitude [degrees_east]"],
                                          filter_data["Latitude [degrees_north]"])

# Считаем градиент абсолютной солёности (aka dSA)
filter_data["dSA"] = vertical_salinity_gradient(filter_data["SA"].tolist(), filter_data["Depth [m]"].tolist())

filter_data.to_csv("res.csv")


x = filter_data["Depth [m]"]
a = filter_data["SA"]
b = filter_data["SP"]
c = filter_data["dSA"]

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
scatter1 = ax1.scatter(list(x) * 2, list(a) + list(b), c=[1 for _ in range(len(a))] + [2 for _ in range(len(a))])
scatter2 = ax2.bar(x, c, color=['green' if y > 0 else 'red' for y in list(c)])

plt.show()
