import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из CSV файла
df = pd.read_csv('Laba 5.csv')

# 1) Линейный график общей прибыли за все месяцы (синий, не пунктирный)
plt.figure(figsize=(8, 5))
plt.plot(df['month_number'], df['total_profit'],
         linestyle='-', color='blue',
         label='Общая прибыль')
plt.xlabel('Номер месяца')
plt.ylabel('Общая прибыль')
plt.title('Общая прибыль по месяцам')
plt.legend(loc='lower right')
plt.show()

# 2) Линейный график количества проданных единиц (пунктирный с чёрными точками)
plt.figure(figsize=(8, 5))
plt.plot(df['month_number'], df['total_units'],
         linestyle='--', linewidth=2, marker='o',
         markerfacecolor='black', color='red',
         markersize=6, label='Продажи (ед.)')
plt.xlabel('Номер месяца')
plt.ylabel('Количество проданных единиц')
plt.title('Продажи по месяцам')
plt.legend()
plt.show()

# 3) Графики продаж каждого продукта на одном графике (толстые линии с точками)
plt.figure(figsize=(10, 6))
products = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']
markers = ['o', 's', '^', 'D', 'p', '*']  # разные маркеры для каждого продукта

for product, marker in zip(products, markers):
    plt.plot(df['month_number'], df[product],
             linewidth=2, marker=marker,
             markersize=6, label=product)

plt.xlabel('Номер месяца')
plt.ylabel('Продажи (ед.)')
plt.title('Продажи продуктов по месяцам')
plt.legend()
plt.show()

# 4) Отдельные графики для каждого продукта (точки и толстые линии)
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Продажи продуктов по месяцам')

for i, product in enumerate(products):
    row = i // 3
    col = i % 3
    axes[row, col].plot(df['month_number'], df[product],
                        linewidth=3, marker='o',
                        markersize=6)
    axes[row, col].set_title(product)
    axes[row, col].set_xlabel('Номер месяца')
    axes[row, col].set_ylabel('Продажи (ед.)')

plt.tight_layout()
plt.show()

# 5) Точечный график продаж зубной пасты (оставляем без изменений)
plt.figure(figsize=(8, 5))
plt.scatter(df['month_number'], df['toothpaste'], label='Зубная паста')
plt.xlabel('Номер месяца')
plt.ylabel('Количество проданных единиц')
plt.title('Продажи зубной пасты')
plt.grid(linestyle='--')
plt.legend()
plt.show()

# 6) Столбчатая диаграмма для facecream и facewash (оставляем без изменений)
plt.figure(figsize=(10, 6))
width = 0.4
plt.bar(df['month_number'] - width / 2, df['facecream'], width=width, label='Face Cream')
plt.bar(df['month_number'] + width / 2, df['facewash'], width=width, label='Face Wash')
plt.xlabel('Номер месяца')
plt.ylabel('Продажи (ед.)')
plt.title('Продажи Face Cream и Face Wash')
plt.legend()
plt.show()

# 7) Круговая диаграмма общих продаж по продуктам (добавляем легенду)
total_sales = df[products].sum()
plt.figure(figsize=(8, 8))
patches, texts, autotexts = plt.pie(total_sales,
                                    labels=products,
                                    autopct='%1.1f%%',
                                    startangle=90)
plt.legend(patches, products,
           loc="center left",
           bbox_to_anchor=(1, 0, 0.5, 1))
plt.title('Доля продаж продуктов за год')
plt.tight_layout()
plt.show()

# 8) Слоеная диаграмма продаж всех продуктов (оставляем без изменений)
plt.figure(figsize=(10, 6))
plt.stackplot(df['month_number'],
              df['facecream'], df['facewash'],
              df['toothpaste'], df['bathingsoap'],
              df['shampoo'], df['moisturizer'],
              labels=products)
plt.xlabel('Номер месяца')
plt.ylabel('Продажи (ед.)')
plt.title('Продажи всех продуктов по месяцам')
plt.legend(loc='upper left')
plt.show()
