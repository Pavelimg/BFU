from itertools import permutations

print(len(list(map(lambda x: "".join(x), permutations("АБРАКАДАБРА", 6)))))
