import matplotlib.pyplot as plt
import pandas


def interpolation(d, x):
    output = d[0][1] + (x - d[0][0]) * ((d[1][1] - d[0][1]) / (d[1][0] - d[0][0]))
    return output



plt.style.use('_mpl-gallery')

file_path = 'data2.csv'
input_data = pandas.read_csv(file_path, sep=";")


print(input_data)
xs, ys, zs = [],[],[]
for i in range(31):
    for j in range(23):
        if input_data[str(j)].loc[input_data.index[i]] != "nan":
            zs.append(input_data[str(j)].loc[input_data.index[i]])
            xs.append(j)
            ys.append(i)

fig, axes = plt.subplots(nrows=2, ncols=2, subplot_kw={"projection": "3d"})

axes[0][0].scatter(xs, ys, zs)



plt.show()
