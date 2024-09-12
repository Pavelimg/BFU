K, L, M = 0, 2, 2
n = 100_000

# На вход дается одно число х, нужно вывести все числа от 1 до х, удовлетворяющие условию:
# 3^K + 5^L + 7^M = Xi

for a in range(K + 1):
    for b in range(L + 1):
        for c in range(M + 1):  # перебираем все комбинации K, L, M
            result = (3 ** a) * (5 ** b) * (7 ** c)
            if result > n:
                break
            print(F'3^{a} * 5^{b} * 7^{c} = {result}')
