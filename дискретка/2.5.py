x_size = 19
y_size = 16

matrix = [[0 for _ in range(x_size)] for _ in range(y_size)]
for i in reversed(matrix):
    print(i)

for y in range(y_size):
    for x in range(x_size):
        if x == 0 and y == 0:
            matrix[y][x] = 1
        elif x == 0:
            matrix[y][x] = matrix[y - 1][x]
        elif y == 0:
            matrix[y][x] = matrix[y][x - 1]

        else:
            matrix[y][x] = matrix[y - 1][x] + matrix[y][x - 1]

print()
for i in reversed(matrix):
    print(i)
