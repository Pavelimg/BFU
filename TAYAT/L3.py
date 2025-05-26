def homski(n, string="S"):
    string = string.replace("S", "AB")  # S → AB
    for _ in range(n):  # A → CE
        string = string.replace("A", "CE")  # A → CE
        string = string.replace("E", "AD")  # E → AD
    string = string.replace("A", ".")  # A → .
    string = string.replace("B", "GD")  # B → 001
    string = string.replace("G", "CC")  # G → CC
    string = string.replace("C", "0")  # C → 0
    string = string.replace("D", "1")  # D → 1
    return string


def greybax(n, string="S"):
    string = string.replace("S", "0ACB")  # S → AB
    for _ in range(n - 1):  # A → 0AC
        string = string.replace("A", "0AC")
    string = string.replace("A", ".")  # B → 0DC
    string = string.replace("B", "0DC")  # B → 0DC
    string = string.replace("C", "1")  # C → 1
    string = string.replace("D", "0")  # D → 0
    return string


for i in range(1, 20, 3):
    print(f"n = {i} | Хомский = {homski(i)}| Грейбах = {greybax(i)}")

